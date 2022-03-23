import tkinter as tk

class AddComponentScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Component Screen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Login page",
                           command=lambda: controller.show_frame("LoginScreen"))
        button.pack()