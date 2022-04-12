"""Test module for ReactComponentViewer"""
import unittest
from ..database import Database


class TestMaksukortti(unittest.TestCase):
    """Set up"""

    def setUp(self):
        print("Set up goes here")

    def test_db(self):
        """Adding user test"""
        database = Database()
        database.add_user('root', 'root')
        self.assertEqual(database.verify_password('root', 'root'), True)
