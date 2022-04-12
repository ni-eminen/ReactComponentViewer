"""Test module for ReactComponentViewer"""
import unittest

from src.util.user import User
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

    def test_user_stringify(self):
        """Test user stringify"""
        user = User('username')
        self.assertEqual(user.stringify(), f"username: username id: {user.user_id} \
                logged in: False")

    def test_user_name_change(self):
        """Tests user name changing"""
        user = User('username')
        user.change_username('us')
        self.assertEqual(user.username, 'us')
