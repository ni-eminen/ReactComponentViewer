import tkinter as tk
from tkinter import Button, Frame, Canvas, Widget

class AddComponentScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = Frame(self,bg='blue')
        mainframe.grid(row=0, column=0, sticky='nsew')

        # Make the buttons with the icons to be shown
        # home_b = Button(frame,bg='orange',relief='flat')
        # set_b = Button(frame,bg='orange',relief='flat')
        # ring_b = Button(frame,bg='orange',relief='flat')

        # Put them on the frame
        # home_b.grid(row=0,column=0,pady=10)
        # set_b.grid(row=1,column=0,pady=50)
        # ring_b.grid(row=2,column=0)

        # Bind to the frame, if entered or left
        # frame.bind('<Enter>',lambda e: expand())
        # frame.bind('<Leave>',lambda e: contract())
