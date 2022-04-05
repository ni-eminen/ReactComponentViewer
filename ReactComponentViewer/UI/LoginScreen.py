from lib2to3.pgen2.token import COLONEQUAL
import tkinter as tk
from functools import partial
from database import Database


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller, db):
        tk.Frame.__init__(self, parent)
        self.screen_size = '500x700'
        self.db = db
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

        usernameLabel = tk.Label(
            login_div, text="Username", bg='white').grid(row=0, column=0)

        username = tk.StringVar()
        usernameEntry = tk.Entry(
            login_div, textvariable=username, bg='white').grid(row=0, column=1, padx=10, pady=10)

        passwordLabel = tk.Label(
            login_div, text="Password", bg='white').grid(row=1, column=0)

        password = tk.StringVar()
        passwordEntry = tk.Entry(
            login_div, textvariable=password, bg='white').grid(row=1, column=1, padx=10, pady=10)

        # username label and text entry box

        valLogin = partial(self.validateLogin, username, password)
        create_user_ = partial(self.create_user, username, password)

        # login button
        login_b = tk.Button(login_div, text="Login", command=valLogin).grid(
            row=2, column=1, sticky='e', padx=10)

        # login button
        create_account_b = tk.Button(login_div, text="Create account", command=create_user_).grid(
            row=3, column=1, sticky='e', padx=10, pady=5)

    def validateLogin(self, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        isAuth = self.db.verify_password(username.get(), password.get())
        if isAuth:
            self.controller.show_frame("AddComponentScreen")

    def create_user(self, username, password):
        self.db.add_user(username.get(), password.get())
