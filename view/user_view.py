from tkinter import *
from view.comment_view import CommentView
from view.post_view import PostView


class UserView:
    def __init__(self, user):
        self.window = Tk()
        self.window.geometry("300x230")
        self.window.title("User Profile")
        Label(self.window, text=user.name, font=("Arial", 20)).pack()

        if user.status == True:
            Button(self.window, width=8, text="Post", command=self.open_post_view).place(x=40, y=100)
            Button(self.window, width=8, text="Like", command=self.open_like_view).place(x=120, y=100)
            Button(self.window, width=8, text="Comment", command=self.open_comment_view).place(x=200, y=100)
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
        pass
