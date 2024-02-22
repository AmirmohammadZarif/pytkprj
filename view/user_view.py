from tkinter import *
from view.comment_view import CommentView
from view.post_view import PostView
from view.like_view import LikeView


class UserView:
    def __init__(self, user):
        self.window = Tk()
        self.window.geometry("300x230")
        self.window.title("User Profile")
        l1 = Label(self.window, text=user.name, font=("Arial", 20))
        l1.grid(row = 1, column = 2, sticky = N)


        if user.status == True:
            b1 = Button(self.window, width=8, text="+", command=self.open_post_view)
            b2 = Button(self.window, width=8, text="👍", command=self.open_like_view)
            b3 = Button(self.window, width=8, text="💬", command=self.open_comment_view)
            b1.grid(row = 2, column = 1, sticky = E)
            b2.grid(row = 2, column = 2, sticky = E)
            b3.grid(row = 2, column = 3, sticky = E)
        else:
            Label(self.window, text="Suspended Account", font=("Arial", 20)).pack()

        self.window.mainloop()

    def open_post_view(self):
        self.window.destroy()
        PostView()

    def open_comment_view(self):
        self.window.destroy()
        CommentView()

    def open_like_view(self):
        self.window.destroy()
        LikeView()
