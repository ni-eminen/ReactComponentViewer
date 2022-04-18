"""User class module"""


class User:
    """User class
    Attributes:
        username: string
    """

    def __init__(self, username=''):
        self.username = username
        self.user_id = 0
        self.logged_in = False
        self.components = []

    def stringify(self):
        """Stringify user"""
        return f"username: {self.username} id: {self.user_id} \
                logged in: {self.logged_in}"

    def change_username(self, new_username):
        """Changes the users username

        Args:
            new_username (string): New username
        """
        self.username = new_username

    def patch_component(self, component_id, component_string):
        """Patches a component in users components

        Args:
            component_id (number): Id of the component
            component_string (string): New component string
        """
        print(component_string)
        for component in self.components:
            if component[2] == component_id:
                i = self.components.index(component)
                self.components[i][1] = component_string
