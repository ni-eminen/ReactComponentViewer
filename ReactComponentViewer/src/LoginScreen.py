import tkinter as tk
from functools import partial


class LoginScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        usernameLabel = tk.Label(self, text="User Name").grid(row=0)

        # username label and text entry box
        username = tk.StringVar()
        usernameEntry = tk.Entry(
            self, textvariable=username).grid(row=0, column=1)

        # #password label and password entry box
        passwordLabel = tk.Label(self, text="Password").grid(row=1, column=0)
        password = tk.StringVar()
        passwordEntry = tk.Entry(
            self, textvariable=password, show='*').grid(row=1, column=1)

        valLogin = partial(self.validateLogin, username, password)

        # #login button
        loginButton = tk.Button(self, text="Login", command=valLogin).grid(
            row=2, column=1, sticky='e')

    def validateLogin(self, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        if True:
            self.controller.show_frame("AddComponentScreen")
