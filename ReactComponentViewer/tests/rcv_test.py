import unittest
from database import Database

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_hello_world(self):
        Database.add_user('root', 'root')
        self.assertEqual(Database.verify_password('root', 'root'), True)