"""Test module for ReactComponentViewer"""
import unittest
from src.util.utilities import render_component, row_as_array


class TestUtil(unittest.TestCase):
    """Set up"""

    def setUp(self):
        print("Set up goes here")

    def test_render_component_good(self):
        """Testing that a component can be sent to the back end, which consecutively
        responds with an HTML file"""
        react_component = render_component('return <h1>asdf</h1>', True)
        self.assertEqual(react_component.text[0:15], '<!DOCTYPE html>')

    def test_render_component_bad(self):
        """Sending an incorrect component to the backend. Regardless of the input 
        we should receive an HTML file indicating that the backend is functional."""
        react_component = render_component('return h1>asdf</h1>', True)
        self.assertEqual(react_component.text[0:15], '<!DOCTYPE html>')

    def test_row_as_array(self):
        """Row as array makes arrays returned by the database mutable."""
        rows_as_array = row_as_array([[123], [234], [345]])
        rows_as_array[1] = 555
        self.assertEqual(rows_as_array[1], 555  )



