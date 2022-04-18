"""Module for add component screen"""
import tkinter as tk
from tkinter import END, Button, Frame, Text, Toplevel
from src.util.utilities import render_component

POP = None


class AddComponentScreen(tk.Frame):
    """Class for add component screen"""

    def save_component(self, name, component):
        """Asks db class to save a component.

        Args:
            name (string): Name for the component
            component (string): The component
        """
        self.controller.database.save_component(
            name, self.controller.user.user_id, component)
        POP.destroy()

    def save_component_dialog(self, component):
        """Opens a dialog for saving component

        Args:
            component (string): The component that will be saved.
        """
        global POP  # pylint: disable=global-statement
        POP = Toplevel(self)
        POP.title('Save component')
        POP.geometry('400x400')
        POP.config(background='white')

        frame = tk.Frame(POP, background='white', pady=20)

        name_label = tk.Label(
            frame, text='Component name:', background='white')
        ok_button = tk.Button(
            frame, text='OK', command=lambda: self.save_component(name_var.get(), component))
        cancel_button = tk.Button(
            frame, text='Cancel', command=lambda: POP.destroy())  # pylint: disable=unnecessary-lambda

        name_var = tk.StringVar()
        name_entry = tk.Entry(frame, textvariable=name_var)

        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1, columnspan=2)
        ok_button.grid(row=1, column=2, sticky='e', pady=10)
        cancel_button.grid(row=1, column=1, sticky='e', pady=10)

        frame.pack()

    def __init__(self, parent, controller):
        """Initializes the add component screen.

        Args:
            parent: Parent frame.
            controller (Tk): Controller for state.
        """

        placeholder = """const [counter, setCounter] = useState(0);

return (
<div>
    <h1>{counter}</h1>
    <button onClick={() => setCounter(counter + 1)}>click me</button>
</div>
);"""

        tk.Frame.__init__(self, parent)
        self.screen_size = '1000x700'
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = Frame(self, bg='red')
        mainframe.grid(row=0, column=0, sticky='nsew')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        # mainframe.grid_rowconfigure(1, weight=1)

        text_frame = Frame(mainframe, bg='black')
        text_frame.grid(column=0, row=0, sticky='news')

        text_editor = Text(text_frame)
        text_editor.insert('1.0', placeholder)
        text_editor.pack(side='top', fill='both', expand=True)

        button_frame = Frame(mainframe, bg='white')
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid(column=0, row=1, sticky='nswe')

        render_button = Button(button_frame, command=lambda: render_component(
            text_editor.get('1.0', END)), text='Render component')
        render_button.grid(column=0, row=0, sticky='e')

        save_button = Button(button_frame, command=lambda: self.save_component_dialog(
            text_editor.get('1.0', END)), text="Save component")
        save_button.grid(column=1, row=0, sticky="e")
