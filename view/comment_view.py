from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller import *
from model.entity.comment import Comment
from model.entity.like import Like
from model.entity.post import Post
from model.entity.user import User
from controller.comment_controller import *

class CommentView():
    def __init__(self):
        self.win_comment = Tk()
        self.win_comment.geometry("1100x400")
        self.win_comment.title("Comment Feed")
        self.controller = CommentController()

        Label(self.win_comment, text="Comment Id").place(x=20, y=20)
        self.comment_id = IntVar()
        Entry(self.win_comment, state="readonly", textvariable=self.comment_id).place(x=120, y=20)

        Label(self.win_comment, text="Comment Text").place(x=20, y=60)
        self.comment_text = StringVar()
        Entry(self.win_comment, textvariable=self.comment_text).place(x=120, y=60)

        Label(self.win_comment, text="username").place(x=20, y=100)
        self.username = StringVar()
        Entry(self.win_comment, state="readonly", textvariable=self.username).place(x=120, y=100)

        Label(self.win_comment, text="Post ID").place(x=20, y=140)
        self.post_id = StringVar()
        Entry(self.win_comment, state="readonly", textvariable=self.post_id).place(x=120, y=140)

        Label(self.win_comment, text="Post Text").place(x=20, y=180)
        self.post_text = StringVar()
        Entry(self.win_comment, state="readonly", textvariable=self.post_text).place(x=120, y=180)

        self.table = ttk.Treeview(self.win_comment, columns=(1, 2, 3, 4, 5), show="headings")

        self.table.column(1, width=80)
        self.table.column(2, width=300)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=300)

        self.table.heading(1, text="Comment ID")
        self.table.heading(2, text="Comment Text")
        self.table.heading(3, text="UserName")
        self.table.heading(4, text="Post ID")
        self.table.heading(5, text="Post Text")

        self.table.bind("<<TreeviewSelect>>", self.Select_Comment)

        Button(self.win_comment, text="Save", width=8, command=self.Save_Click).place(x=20, y=300)
        Button(self.win_comment, text="Edit", width=8, command=self.Edit_Click).place(x=100, y=300)
        Button(self.win_comment, text="Remove", width=8, command=self.Remove_Click).place(x=180, y=300)
        Button(self.win_comment, text="New Comment", width=14, command=self.reset_form).place(x=80, y=250)


        self.table.place(x=250, y=18)

        self.reset_form()
        self.win_comment.mainloop()


    def Save_Click(self):
        message = self.controller.save(self.comment_text.get(), PostController.current_post,UserController.current_user)
        msg.showinfo("Save", message)
        self.reset_form()


    def Edit_Click(self):
        if self.username.get() == UserController.current_user.username:
            message = self.controller.edit(self.comment_id.get(),self.comment_text.get(), PostController.current_post,UserController.current_user)
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Error", "This Post Doesnt Belong to You")
        self.reset_form()

    def Remove_Click(self):
        if self.username.get() == UserController.current_user.username:
            self.controller.remove(self.comment_id.get())
            msg.showinfo("removed", "Post was removed")
        else:
            msg.showerror("Error", "This Post Doesnt Belong to You")
        self.reset_form()

    def reset_form(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for comment in self.controller.get_comments_sorted_by_date_and_post_id():
            self.table.insert("", END, values=[comment.id, comment.text, comment.user.username, comment.post.id,comment.post.text])

        self.comment_id.set("")
        self.comment_text.set("")
        self.username.set(UserController.current_user.username)
        self.post_id.set(PostController.current_post.id)
        self.post_text.set(PostController.current_post.text)

    def Select_Comment(self, event):
        selected_item = self.table.focus()
        comment = self.table.item(selected_item, "values")
        if comment:
            self.comment_id.set(comment[0])
            self.comment_text.set(comment[1])
            self.username.set(comment[2])
            self.post_id.set(comment[3])
            self.post_text.set(comment[4])
            CommentController.current_comment = CommentController.find_by_id(comment[0])
            PostController.current_post = PostController.find_by_id(comment[3])
