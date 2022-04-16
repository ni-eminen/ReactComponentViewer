"""Module for components window"""
import tkinter as tk
from src.util.utilities import render_component


class ComponentsScreen(tk.Frame):
    """Class for components window"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.collection = 'user_components'
        self.components = []
        self.screen_size = '1000x700'
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        components_frame = tk.Frame(self, background='black')
        components_frame.grid_columnconfigure(0, weight=1)
        components_frame.grid_rowconfigure(0, weight=1)
        components_frame.grid(column=0, row=0, sticky='nsew', rowspan=2)
        self.components_list = tk.Listbox(components_frame)

        self.components_list.bind("<<ListboxSelect>>", self.listbox_onselect)
        self.components_list.grid(row=0, column=0, sticky='nsew')

        component_frame = tk.Frame(self, background='white')
        component_frame.grid(column=1, row=0, sticky='nsew')

        component_frame.grid_columnconfigure(0, weight=1)
        component_frame.grid_rowconfigure(0, weight=1)

        buttons_frame = tk.Frame(self, background='white')
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid(row=1, column=1, sticky='nsew')

        self.component_text = tk.Text(component_frame)
        self.component_text.grid(row=0, sticky='nsew')

        render_button = tk.Button(buttons_frame, command=lambda: render_component(
            self.component_text.get('1.0', tk.END)), text='Render component')
        render_button.grid(column=1, row=1, sticky='e')

        save_changes_button = tk.Button(
            buttons_frame, text='Save changes', command=lambda: self.save_changes())  # pylint: disable=unnecessary-lambda

        save_changes_button.grid(column=0, row=1, sticky='e')

    def save_changes(self):
        """Saves changes to current component"""
        new_text = self.component_text.get('1.0', tk.END)
        selected_name = self.components_list.get(tk.ANCHOR)
        selected = None
        for component in self.components:
            if component[0] == selected_name:
                selected = component
                break

        if selected is None:
            return None

        component_id = selected[2]
        self.controller.database.patch_component(
            component_id, new_text)

        if self.collection == 'user_components':
            self.components = self.controller.database.get_user_components(
                self.controller.user.user_id)

        return new_text

    def load_components(self, components):
        """Loads the component listbox with the components given"""
        self.components = components
        self.components_list.delete(0, tk.END)
        for component in components:
            self.components_list.insert(tk.END, component[0])

    def listbox_onselect(self, _select):
        """Sets the component text on display"""
        self.component_text.delete('1.0', tk.END)
        component_text = ''
        selected = self.components_list.get(tk.ANCHOR)
        for component in self.components:
            if component[0] == selected:
                component_text = component[1]

        self.component_text.insert('1.0', component_text)
