"""Utilities class module"""
import webbrowser
import requests
import numpy as np


def render_component(component, test=False):
    """Sends a component to the backend to be built into a react app.
    Displays it in a webbrowser.

    Args:
        component (string): Component in string format.
        test (bool, optional): If this is a test run or not. Defaults to False.

    Returns:
        string: Returns the html file generated.
    """
    url = 'http://157.230.120.211:49160/api/component'
    string_json = '{{"component": "{c}"}}'.format(  # pylint: disable=consider-using-f-string
        c=component.replace('\n', '').replace('"', "'"))
    headers = {'content-type': 'application/json'}
    react_build = requests.post(
        url, data=string_json, headers=headers)

    if not test:
        with open("react_build.html", "w", encoding='utf8') as file:
            file.write(react_build.text)
            file.close()
            webbrowser.open_new("react_build.html")

    return react_build


def row_as_array(rows):
    """LegacyRow as an array. This gives the row mutability.

    Args:
        rows (LegacyRow): Rows that will be converted to an array.

    Returns:
        ndarray: An array
    """
    new_arr = []
    for row in rows:
        new_arr.append(np.asarray(row).tolist())
    return new_arr
