"""Module for components window"""
import tkinter as tk
from src.util.utilities import render_component


class ComponentsScreen(tk.Frame):
    """Class for components window"""

    def __init__(self, parent, controller):
        """Initializes components screen.

        Args:
            parent (Frame): Parent Frame for this Frame.
            controller (Tk): Controller for state.
        """
        tk.Frame.__init__(self, parent)
        self.collection = 'user'
        self.components = []
        self.screen_size = '1000x700'
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        components_frame = tk.Frame(self, background='white')
        components_frame.grid_columnconfigure(0, weight=1)
        components_frame.grid_columnconfigure(1, weight=1)
        components_frame.grid_rowconfigure(1, weight=1)
        components_frame.grid(column=0, row=0, sticky='nsew', rowspan=2)
        self.components_list = tk.Listbox(components_frame)

        self.components_list.bind("<<ListboxSelect>>", self.listbox_onselect)
        self.components_list.grid(row=1, column=0, columnspan=2, sticky='nsew')

        commmunity_button = tk.Button(
            components_frame, text='community', command=lambda: self.load_community_components())
        user_button = tk.Button(
            components_frame, text='user', command=lambda: self.load_user_components())

        commmunity_button.grid(
            row=0, column=0, sticky='nsew')
        user_button.grid(row=0, column=1, sticky='nsew')

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
        render_button.grid(column=2, row=1, sticky='e')

        save_changes_button = tk.Button(
            buttons_frame, text='Save changes', command=lambda: self.save_changes())
        save_changes_button.grid(column=1, row=1, sticky='e')

        delete_component_button = tk.Button(
            buttons_frame, text='Delete component', command=lambda: self.delete_component(
                self.components_list.get(tk.ANCHOR)))
        delete_component_button.grid(row=1, column=0)

    def delete_component(self, component_name):
        """Deletes a component.

        Args:
            component_name (string): Component's name
        """
        component_id = self.controller.database.get_component_id(
            component_name)
        self.controller.database.delete_component(component_id)
        self.controller.user.components = self.controller.database.get_user_components(
            self.controller.user.user_id)
        if self.collection == 'user':
            self.load_user_components()
        else:
            self.load_community_components()
        self.component_text.delete('1.0', tk.END)

    def save_changes(self):
        """Saves changes to current component.

        Returns:
            string: The saved text
        """
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

        if self.collection == 'user':
            self.components = self.controller.database.get_user_components(
                self.controller.user.user_id)

        return new_text

    def load_components(self, components):
        """Loads the component listbox with the components given.

        Args:
            components (ndarray): Components list
        """
        self.components = components
        self.components_list.delete(0, tk.END)
        for component in components:
            self.components_list.insert(tk.END, component[0])

    def load_community_components(self):
        """Loads the community components.
        """
        self.collection = 'community'
        components = self.controller.database.get_community_components()
        self.load_components(components)

    def load_user_components(self):
        """Loads the user's components on to the components listbox.
        """
        self.collection = 'user'
        components = self.controller.database.get_user_components(
            self.controller.user.user_id)
        self.load_components(components)

    def listbox_onselect(self, _select):
        """Sets the component text on display."""
        self.component_text.delete('1.0', tk.END)
        component_text = ''
        selected = self.components_list.get(tk.ANCHOR)
        for component in self.components:
            if component[0] == selected:
                component_text = component[1]

        self.component_text.insert('1.0', component_text)
