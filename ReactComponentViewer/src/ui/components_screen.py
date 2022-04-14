"""Module for components window"""
import tkinter as tk


class ComponentsScreen(tk.Frame):
    """Class for components window"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.screen_size = '1000x700'
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        components_frame = tk.Frame(self, background='black')
        components_frame.grid_columnconfigure(0, weight=1)
        components_frame.grid_rowconfigure(0, weight=1)
        components_frame.grid(column=0, row=0, sticky='nsew')
        self.components_list = tk.Listbox(components_frame)

        self.components_list.grid(row=0, column=0, sticky='nsew')

        component_frame = tk.Frame(self, background='yellow')
        component_frame.grid(column=1, row=0, sticky='nsew')

        component_frame.grid_columnconfigure(0, weight=1)
        component_frame.grid_rowconfigure(0, weight=1)
        component_frame.grid_rowconfigure(1, weight=1)

        component_text = tk.Text(component_frame)
        component_text.grid(row=0, sticky='nsew')

    def load_components(self, components):
        """Loads the component listbox with the components given"""
        for component in components:
            self.components_list.insert(tk.END, component[0])

        print('components loaded')
