"""Module for components window"""
import tkinter as tk


class ComponentsScreen(tk.Frame):
    """Class for components window"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.screen_size = '1000x700'
        self.controller = controller
        label = tk.Label(self, text="Your Components Screen",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the 'Login screen'",
                           command=lambda: controller.show_frame("LoginScreen"))
        button.pack()