import tkinter as tk
from tkinter import END, Button, Frame, Canvas, Widget, Text
import webview
import requests
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import pygments

class AddComponentScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = Frame(self,bg='red')
        mainframe.grid(row=0, column=0, sticky='nsew')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        mainframe.grid_rowconfigure(1, weight=1)

        text_frame = Frame(mainframe, bg='black')
        text_frame.grid(column=0, row=0, sticky='news')

        text_editor = Text(text_frame)
        text_editor.pack(side='top', fill='both', expand=True)

        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)

        cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

        # These five lines are optional. If omitted, default colours are used.
        cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
        cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
        cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}
        ip.Percolator(text_editor).insertfilter(cdg)

        button_frame = Frame(mainframe, bg='red')
        button_frame.grid(column=0, row=1, sticky='nswe')

        render_button = Button(button_frame, command=lambda: render_component(text_editor.get('1.0', END)), text='Render component')
        render_button.grid(column=0, row=0, sticky='e')


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

        def render_component(component):
            print(component)
            url = 'http://www.localhost:3000/api/component'
            string_json = '{{"component": "{c}"}}'.format(c=component).replace('\n', '')
            headers = {'content-type': 'application/json'}

            

            print()
            print()
            print()
            print(string_json)
            print()
            
            print()
            print()
            print()

            react_build = requests.post(url, data = string_json, headers=headers)

            f = open("react_build.html", "w")
            f.write(react_build.text)
            f.close()


            # Create a GUI window to view the HTML content
            webview.create_window('build', "react_build.html")
            webview.start()
