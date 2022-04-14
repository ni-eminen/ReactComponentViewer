"""Login screen module"""
import tkinter as tk
from functools import partial

from src.util.user import User


class LoginScreen(tk.Frame):
    """Login screen"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.screen_size = '500x700'
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = tk.Frame(self, bg='white')
        mainframe.grid(row=0, column=0, sticky='nsew')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        mainframe.grid_rowconfigure(1, weight=10)

        login_div = tk.Frame(mainframe, bg='white')
        login_div.grid(row=0, column=0)

        tk.Label(
            login_div, text="Username", bg='white').grid(row=0, column=0)

        username = tk.StringVar()
        tk.Entry(
            login_div, textvariable=username, bg='white').grid(row=0, column=1, padx=10, pady=10)

        tk.Label(
            login_div, text="Password", bg='white').grid(row=1, column=0)

        password = tk.StringVar()
        tk.Entry(
            login_div, textvariable=password, show="*",
            bg='white').grid(row=1, column=1, padx=10, pady=10)

        # username label and text entry box

        val_login = partial(self.log_in_init, username, password)
        create_user_ = partial(self.create_user, username, password)

        # login button
        tk.Button(login_div, text="Login", command=val_login).grid(
            row=2, column=1, sticky='e', padx=10)

        # login button
        tk.Button(login_div, text="Create account", command=create_user_).grid(
            row=3, column=1, sticky='e', padx=10, pady=5)

    def log_in_init(self, username, password):
        """Perform necessary actions to log the user in and initialize the application"""
        self.validate_login(username, password)
        self.controller.show_frame("AddComponentScreen")
        self.controller.user.components = self.controller.database.get_user_components(
            self.controller.user.user_id)
        print('fasfda', self.controller.user.components)

    def validate_login(self, username, password):
        """Validates the username and password"""
        is_auth = self.controller.database.verify_password(
            username.get(), password.get())
        if is_auth:
            user = User(username.get())
            user.user_id = self.controller.database.get_user_id(
                user.username)
            user.logged_in = True
            self.controller.user = user

    def create_user(self, username, password):
        """Adds user to the database"""
        self.controller.database.add_user(username.get(), password.get())
