"""User class module"""

class User:
    """User class"""
    def __init__(self, username=''):
        self.username = username
        self.user_id = 0
        self.logged_in = False

    def stringify(self):
        """Stringify user"""
        return f"username: {self.username} id: {self.user_id} \
                logged in: {self.logged_in}"

    def change_username(self, new_username):
        """Changes username"""
        self.username = new_username
