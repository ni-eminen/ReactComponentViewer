"""Module for add component screen"""
import webbrowser
import tkinter as tk
from tkinter import END, Button, Frame, Text
import requests


class AddComponentScreen(tk.Frame):
    """Class for add component screen"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.screen_size = '1000x700'
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = Frame(self, bg='red')
        mainframe.grid(row=0, column=0, sticky='nsew')
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)
        mainframe.grid_rowconfigure(1, weight=1)

        text_frame = Frame(mainframe, bg='black')
        text_frame.grid(column=0, row=0, sticky='news')

        text_editor = Text(text_frame)
        text_editor.insert('1.0', """asdf""")
        text_editor.pack(side='top', fill='both', expand=True)

        button_frame = Frame(mainframe, bg='red')
        button_frame.grid(column=0, row=1, sticky='nswe')

        render_button = Button(button_frame, command=lambda: render_component(
            text_editor.get('1.0', END)), text='Render component')
        render_button.grid(column=0, row=0, sticky='e')

        def render_component(component):
            print(component)
            url = 'http://157.230.120.211:49160/api/component'
            string_json = '{{"component": "{c}"}}'.format( # pylint: disable=consider-using-f-string
                c=component).replace('\n', '')
            headers = {'content-type': 'application/json'}
            react_build = requests.post(url, data=string_json, headers=headers)

            with open("react_build.html", "w", encoding='utf8') as file:
                file.write(react_build.text)
                file.close()
                webbrowser.open_new_tab("react_build.html")