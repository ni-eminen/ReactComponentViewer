# Import the required libraries
from tkinter import *
import webview
import requests

url = 'http://www.localhost:3000/api/component'
myobj = {'component': '<a>link</a>'}
x = requests.post(url, data = myobj)
print(x)

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a GUI window to view the HTML content
webview.create_window('build', 'build/index.html')
webview.start()