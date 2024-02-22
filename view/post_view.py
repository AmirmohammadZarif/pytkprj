from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.comment_controller import CommentController
from controller.post_controller import PostController
from controller.user_controller import UserController
from controller.like_controller import *

from model.entity import *
from view.comment_view import CommentView
from view.like_view import LikeView

class PostView():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("740x300")
        self.win.title("Post Feed")
        self.controller = PostController()

        Label(self.win, text="Post Id").place(x=20, y=20)
        self.id = IntVar()
        Entry(self.win, state="readonly", textvariable=self.id).place(x=100, y=20)

        Label(self.win, text="text").place(x=20, y=60)
        self.text = StringVar()
        Entry(self.win, textvariable=self.text).place(x=100, y=60)

        Label(self.win, text="Username").place(x=20, y=100)
        self.username = StringVar()
        Entry(self.win, state="readonly", textvariable=self.username).place(x=100, y=100)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3), show="headings")

        self.table.column(1, width=60)
        self.table.column(2, width=300)
        self.table.column(3, width=100)

        self.table.heading(1, text="Post ID")
        self.table.heading(2, text="Text")
        self.table.heading(3, text="Username")

        self.table.bind("<<TreeviewSelect>>", self.Select_Post)

        Button(self.win, text="Save", width=8, command=self.Save_Click).place(x=20, y=200)
        Button(self.win, text="Edit", width=8, command=self.Edit_Click).place(x=150, y=200)
        Button(self.win, text="Remove", width=8, command=self.Remove_Click).place(x=180, y=200)
        Button(self.win, text="+", width=8, command=self.reset_form).place(x=100, y=150)
        Button(self.win, text="💬", width=8, command=self.Comment_Click).place(x=20, y=150)
        Button(self.win, text="❤️", width=8, command=self.Like_Click).place(x=180, y=150)

        self.table.place(x=10, y=250)

        self.reset_form()
        self.win.mainloop()

    def Save_Click(self):
        message = self.controller.save(self.text.get(), UserController.current_user)
        msg.showinfo("Save", message)

        self.reset_form()

    def Edit_Click(self):
        if self.username.get() == UserController.current_user.username:
            message = self.controller.edit(self.id.get(), self.text.get(), UserController.current_user)
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Error", "This Post Doesnt Belong to You")
        self.reset_form()

    def Remove_Click(self):
        if self.username.get() == UserController.current_user.username:
            self.controller.remove(self.id.get())
            msg.showinfo("removed", "Post was removed")
        else:
            msg.showerror("Error", "This Post Doesnt Belong to You")
        self.reset_form()

    def reset_form(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for post in self.controller.find_all():
            self.table.insert("", END, values=[post.id, post.text, post.user.username])

        self.id.set("")
        self.text.set("")
        self.username.set(UserController.current_user.username)

    def Select_Post(self, event):
        selected_item = self.table.focus()
        post = self.table.item(selected_item, "values")
        if post:
            self.id.set(post[0])
            self.text.set(post[1])
            self.username.set(post[2])

    def Comment_Click(self):
        PostController.current_post = PostController.find_by_id(self.id.get())
        self.win.destroy()
        CommentView()

    def Like_Click(self):
        PostController.current_post = PostController.find_by_id(self.id.get())
        controller = LikeController()
        message = controller.save(PostController.current_post, UserController.current_user)
        msg.showinfo("Liked", message)

        self.win.destroy()
        LikeView()
