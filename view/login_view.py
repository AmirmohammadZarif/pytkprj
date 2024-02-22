from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
from tkinter import ttk
import tkinter as tk
from controller.user_controller import UserController
import tkinter.messagebox as msg
from view.user_view import UserView

class LoginView:
    def __init__(self):
        self.controller = UserController()
        self.window = ThemedTk(theme="clearlooks")
        style = ThemedStyle(self.window)
        style.set_theme("arc")

        self.window.geometry("300x190")
        self.window.title("User Login")

        # username
        ttk.Label(self.window, text="Username").pack()
        self.username = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.username).pack()

        # password
        ttk.Label(self.window, text="Password").pack()
        self.password = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.password).pack()


        # login button
        ttk.Button(self.window, text="Login", command=self.login_click).place(x=125, y=100)

        self.window.mainloop()

    def login_click(self):
        user, error_message = self.controller.find_by_username_and_password(self.username.get(), self.password.get())
        print(UserController.find_all())
        UserController.current_user = user
        if user:
            msg.showinfo("Info", "Successful Login")
            self.window.destroy()
            UserView(user)
        else:
            msg.showerror("Error", error_message)
