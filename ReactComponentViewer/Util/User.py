from database import Database as db


class User:
    def __init__(self, username):
        self.username = username
        self.components = db.get_components_for_user(username)
