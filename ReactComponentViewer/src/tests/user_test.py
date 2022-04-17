"""Test module for ReactComponentViewer"""
import unittest

from src.util.user import User


class TestRCV(unittest.TestCase):
    """Set up"""

    def setUp(self):
        print("Set up goes here")
        self.user = User('username')
        self.user.components = [['', 'component', 1]]

    def test_user_stringify(self):
        """Test user stringify"""
        self.assertEqual(self.user.stringify(), f"username: username id: {self.user.user_id} \
                logged in: False")

    def test_user_name_change(self):
        """Tests user name changing"""
        self.user.change_username('us')
        self.assertEqual(self.user.username, 'us')

    def test_patch_component(self):
        """Test component patching (updating)"""
        self.user.patch_component(1, 'test_component')
        self.assertEqual(self.user.components[0][1], 'test_component')
