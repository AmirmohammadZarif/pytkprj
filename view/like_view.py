from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller import *
from model.entity.comment import Comment
from model.entity.like import Like
from model.entity.post import Post
from model.entity.user import User
from controller.like_controller import *

class LikeView():
    def __init__(self):
        self.win_like = Tk()
        self.win_like.geometry("1100x400")
        self.win_like.title("Likes")
        self.controller = LikeController()

        Label(self.win_like, text="Post Id").place(x=20, y=20)
        self.post_id = IntVar()
        Entry(self.win_like, state="readonly", textvariable=self.post_id).place(x=120, y=20)

        Label(self.win_like, text="Like Id").place(x=20, y=50)
        self.like_id = IntVar()
        Entry(self.win_like, state="readonly", textvariable=self.like_id).place(x=120, y=50)
        
        Label(self.win_like, text="User Id").place(x=20, y=80)
        self.user_id = IntVar()
        Entry(self.win_like, state="readonly", textvariable=self.user_id).place(x=120, y=80)
        
    
        self.table = ttk.Treeview(self.win_like, columns=(1, 2, 3, 4), show="headings")

        self.table.column(1, width=80)
        self.table.column(2, width=300)
        self.table.column(3, width=100)
        self.table.column(4, width=100)


        self.table.heading(1, text="Like ID")
        self.table.heading(2, text="Post Text")
        self.table.heading(3, text="User ID")
        self.table.heading(4, text="Time")

        l1 = Label(self.win_like, text="Likes List", font=("Arial", 20)).place(x=20, y=170)

        self.table.bind("<<TreeviewSelect>>", self.Select_Like)

   
        Button(self.win_like, text="Remove", width=8, command=self.Remove_Click).place(x=180, y=150)

        self.table.place(x=20, y=200)


        l2 = Label(self.win_like, text="Posts Likes Count", font=("Arial", 20)).place(x=20, y=370)

        self.total_table = ttk.Treeview(self.win_like, columns=(1, 2, 3, 4), show="headings")

        self.total_table.column(1, width=80)
        self.total_table.column(2, width=300)
        self.total_table.column(3, width=100)
        self.total_table.column(4, width=100)


        self.total_table.heading(1, text="Post ID")
        self.total_table.heading(2, text="Post Text")
        self.total_table.heading(3, text="User ID")
        self.total_table.heading(4, text="Likes")
        self.total_table.place(x=20, y=400)

        self.reset_form()
        self.win_like.mainloop()


    def Edit_Click(self):
        if self.username.get() == UserController.current_user.username:
            message = self.controller.edit(self.comment_id.get(),self.comment_text.get(), PostController.current_post,UserController.current_user)
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Error", "This Post Doesnt Belong to You")
        self.reset_form()

    def Remove_Click(self):
        if self.user_id.get() == UserController.current_user.id:
            self.controller.remove(self.like_id.get())
            msg.showinfo("removed", "Post was unliked")
        else:
            msg.showerror("Error", "This Like Doesnt Belong to You")
        self.reset_form()

    def reset_form(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for like in self.controller.find_all():
            self.table.insert("", END, values=[like.id, like.post_id, like.user_id, like.date_time])

        post_controller = PostController()
        for post in post_controller.find_all():
            # self.table.insert("", END, values=[post.id, post.text, post.user.username])
            # print(post.id)
            likes = self.controller.find_by_post(post)
            if(likes != "Post Doesn't Exist!!!"):
                self.total_table.insert("", END, values=[post.id, post.text, post.user_id, len(likes)])
          


    def Select_Like(self, event):
        selected_item = self.table.focus()
        likes = self.table.item(selected_item, "values")
        if likes:
            self.like_id.set(likes[0])
            self.post_id.set(likes[1])
            self.user_id.set(likes[2])
            LikeController.current_like = LikeController.find_by_id(likes[0])
