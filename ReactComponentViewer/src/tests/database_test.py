"""Test module for ReactComponentViewer"""
import unittest
import os
from ..database import Database


class TestRCV(unittest.TestCase):
    """Set up"""

    def setUp(self):
        print("Set up goes here")
        if os.path.exists("../../test.db"):
            print(True)
            os.remove("../../test.db")
        self.database = Database('test.db')
        self.database.add_user('root', 'root')

    def test_user_exists(self):
        """Testing that a user can be added to the database"""
        exists = self.database.user_exists('root')
        existsnt = self.database.user_exists('asdf')
        self.assertEqual(exists, True)
        self.assertEqual(existsnt, False)

    def test_add_user(self):
        """Testing user addition"""
        self.database.add_user('test', 'test')
        exists = self.database.user_exists('test')
        self.assertEqual(exists, True)

    def test_verify_password(self):
        """Adding user test"""
        self.database.add_user('test', 'test')
        true = self.database.verify_password('test', 'test')
        false = self.database.verify_password('asdf', 'asdf')
        self.assertEqual(true, True)
        self.assertEqual(false, False)

    def test_save_component(self):
        """Test for component addition"""
        self.database.save_component('test component', 0, 'test component')
        component = self.database.get_user_components(0)[0][0]
        self.assertEqual(component == 'test component', True)

    def test_get_user_id(self):
        """Test for getting a user's id"""
        user_id = self.database.get_user_id('root')
        self.assertEqual(user_id, 1)
