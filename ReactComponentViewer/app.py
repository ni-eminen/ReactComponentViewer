# Import the required libraries
from textwrap import fill
import tkinter as tk
from tkinter import Frame, font as tkfont, Button
from turtle import width  # python 3
from LoginScreen import LoginScreen
from ComponentsScreen import ComponentsScreen
from AddComponentScreen import AddComponentScreen

# url = 'http://www.localhost:3000/api/component'
# myobj = '{"component": "const [num, setNum] = useState(0); return ( <div> <p>{ num }</p> <button onClick={() => setNum(num + 50)}>click me</button> </div> );"}'
# headers = {'content-type': 'application/json'}
# react_build = requests.post(url, data = myobj, headers=headers)

# f = open("react_build.html", "w")
# f.write(react_build.text)
# f.close()


# # Create a GUI window to view the HTML content
# webview.create_window('build', "react_build.html")
# webview.start()

# ----------------------------------------
# sample app

class ReactComponentViewer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('600x600')
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
        home_b = Button(sidebar, command=lambda: self.show_frame(
            'ComponentsScreen'), bg='orange', relief='flat', text='Components')
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

        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = ReactComponentViewer()
    app.mainloop()
