""""This is the """
# Import the required libraries
import tkinter as tk
from tkinter import Frame, font as tkfont, Button
from src.ui.login_screen import LoginScreen
from src.ui.components_screen import ComponentsScreen
from src.database import Database
from src.util.user import User
from src.ui.add_component_screen import AddComponentScreen


class ReactComponentViewer(tk.Tk):
    """This is the main class for ReactComponentViewer. It is responsible for
        setting up the main window and the side bar as well as changing frames."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.user = User()
        self.database = Database()
        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('500x700')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.grid(row=0, column=0, sticky='nsew')
        container.grid_rowconfigure(0, weight=1)

        # sidebar = Frame(container, bg='#89CFF0', width=100)
        # sidebar.grid(row=0, column=0, sticky='nsew')

        # sidebar
        sidebar = tk.Frame(container, width=200, bg='white', height=500,
                           relief='sunken', borderwidth=2)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        # Make the buttons with the icons to be shown
        home_b = Button(sidebar, command=lambda: self.show_components(  # pylint: disable=unnecessary-lambda
        ), bg='orange', relief='flat', text='Components')
        set_b = Button(sidebar, command=lambda: self.show_frame(
            'AddComponentScreen'), bg='orange', relief='flat', text='Add component')

        home_b.pack(pady=10)
        set_b.pack(pady=10)

        content_frame = tk.Frame(container)
        content_frame.pack(fill='both', side='right', expand=True)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginScreen, AddComponentScreen, ComponentsScreen):
            page_name = F.__name__
            frame = F(parent=content_frame, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_login()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        if self.user.logged_in is False:
            return

        frame = self.frames[page_name]
        self.geometry(
            f'{frame.screen_size}+{self.winfo_x()}+{self.winfo_y()-24}')

        frame.tkraise()

    def show_login(self):
        """Raise the login screen"""
        self.frames['LoginScreen'].tkraise()

    def show_components(self):
        """Shows the components screen and loads up the components for it"""
        self.frames['ComponentsScreen'].load_components(
            self.database.get_user_components(self.user.user_id))
        self.show_frame('ComponentsScreen')


if __name__ == "__main__":
    app = ReactComponentViewer()
    app.mainloop()
