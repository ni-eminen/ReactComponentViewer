"""Utilities class module"""
import webbrowser
import requests


def render_component(component):
    """Sends a component to the backend to be built into a react app.
    Displays it in a webbrowser."""
    url = 'http://157.230.120.211:49160/api/component'
    string_json = '{{"component": "{c}"}}'.format(  # pylint: disable=consider-using-f-string
        c=component).replace('\n', '')
    headers = {'content-type': 'application/json'}
    react_build = requests.post(
        url, data=string_json, headers=headers)

    with open("react_build.html", "w", encoding='utf8') as file:
        file.write(react_build.text)
        file.close()
        webbrowser.open_new("react_build.html")
