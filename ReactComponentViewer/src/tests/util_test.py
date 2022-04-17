"""Test module for ReactComponentViewer"""
import unittest
from src.util.utilities import render_component


class TestRCV(unittest.TestCase):
    """Set up"""

    def setUp(self):
        print("Set up goes here")

    def test_render_component(self):
        """Testing that a user can be added to the database"""
        react_component = render_component('return <h1>asdf</h1>', True)
        self.assertEqual(react_component.text[0:15], '<!DOCTYPE html>')
