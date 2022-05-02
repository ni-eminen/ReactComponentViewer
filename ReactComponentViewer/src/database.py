"""Module for database actions"""
import bcrypt
from sqlalchemy import (Column, Table, Integer, String,
                        MetaData, delete, inspect, create_engine, select, insert, update)
from src.util.utilities import row_as_array

SALTROUNDS = 10


class Database:
    """ Database is responsible for creating users and components to
        the database as well as removing them.

        Attributes:
            db_filename: Desired name of the database file."""

    def __init__(self, db_filename='database.db'):
        """Initializes the database with tables.

        Args:
            db_filename (str, optional): Desired name of the database file. 
            Defaults to 'database.db'.
        """
        print('creating connnection')
        self.engine = create_engine(
            f'sqlite:///{db_filename}', echo=False)
        self.conn = self.engine.connect()
        meta = MetaData(bind=self.engine)

        if not inspect(self.engine).has_table('users'):
            Table(
                'users', meta,
                Column('id', Integer, primary_key=True),
                Column('username', String),
                Column('password', String),
            )
        if not inspect(self.engine).has_table('components'):
            Table(
                'components', meta,
                Column('id', Integer, primary_key=True),
                Column('owner_id', Integer),
                Column('component', String),
                Column('name', String)
            )

        meta.reflect()
        self.users_table = meta.tables['users']
        self.components_table = meta.tables['components']

        meta.create_all(self.engine)

    def add_user(self, username, password):
        """Adds a user to the database

        Args:
            username (_type_): Username for the user
            password (_type_): Password for the user

        Returns:
            boolean: Whether user creation was a success or not.
        """

        exists = self.user_exists(username)

        if not exists:
            salt = bcrypt.gensalt(rounds=SALTROUNDS)
            hashed = bcrypt.hashpw(password.encode('utf8'), salt)
            pw_hash = hashed.decode('utf8')

            ins = insert(self.users_table).values(
                username=username, password=pw_hash)
            self.engine.execute(ins)
            return True
        print('User creation failed: User exists')
        return False

    def verify_password(self, username, password):
        """Verifies user password

        Args:
            username (_type_): username
            password (_type_): password

        Returns:
            boolean: Whether the username and password are a match
        """
        users_table = self.users_table

        query = select(users_table.c.password).where(
            users_table.c.username == username)
        hashed = self.conn.execute(query).fetchone()
        if hashed is not None and len(hashed) > 0:
            is_auth = bcrypt.checkpw(password.encode(
                'utf8'), hashed[0].encode('utf8'))
            return is_auth
        return False

    def save_component(self, name, owner_id, component):
        """Saves a component to the database

        Args:
            name (string): Name of the component
            owner_id (_type_): Owner's id
            component (_type_): The component in string format
        """
        ins = insert(self.components_table).values(
            component=component, name=name, owner_id=owner_id)
        self.engine.execute(ins)

    def get_components_for_user(self, username):
        """Gets a users components

        Args:
            username (string): Username

        Returns:
            array: An array of components
        """
        user_id = self.get_user_id(
            username)  # pylint: disable=no-value-for-parameter
        components_table = self.components_table
        query = select(components_table.c.component).where(
            components_table.c.owner_id == user_id)
        components = self.conn.execute(query).fetchall()
        return row_as_array(components)

    def get_component_id(self, component_name):
        """Gets a components id by its name

        Args:
            component_name (string): Name of the component

        Returns:
            number: Id of the component
        """
        query = select(self.components_table.c.id).where(
            self.components_table.c.name == component_name)
        result = self.conn.execute(query).fetchone()
        try:
            return result[0]
        except IndexError as err:
            print(err)
            return None

    def delete_component(self, component_id):
        """Removes a component from the db via id

        Args:
            component_id (number): Id of the component
        """
        query = delete(self.components_table).where(
            self.components_table.c.id == component_id)
        self.conn.execute(query)

    def get_user_id(self, username):
        """Gets a users id by their username

        Args:
            username (string): Username

        Returns:
            number: User id
        """
        query = select(self.users_table.c.id).where(
            self.users_table.c.username == username)
        result = self.conn.execute(query).fetchone()
        if len(result) > 0:
            return result[0]
        return 0

    def get_user_components(self, user_id):
        """Gets a users components

        Args:
            user_id (number): User id

        Returns:
            array: An array of components
        """
        query = select(self.components_table.c.name, self.components_table.c.component,
                       self.components_table.c.id).where(
            self.components_table.c.owner_id == user_id)
        result = self.conn.execute(query).fetchall()

        return row_as_array(result)

    def patch_component(self, component_id, new_component):
        """Updates a component

        Args:
            component_id (number): Id of the component
            new_component (string): New component string
        """
        query = (
            update(self.components_table).
            where(self.components_table.c.id == component_id).
            values(component=new_component)
        )
        print(query)
        self.conn.execute(query)
        print('updated in database')

    def get_community_components(self):
        """Loads the community components

        Returns:
            array: Returns all components
        """
        query = select(self.components_table.c.name, self.components_table.c.component,
                       self.components_table.c.id)
        result = self.conn.execute(query).fetchall()
        return row_as_array(result)

    def user_exists(self, username):
        """Checks if a user is in the database

        Args:
            username (string): Username

        Returns:
            boolean: Whether user exits in the database
        """
        query = select(self.users_table.c.username).where(
            self.users_table.c.username == username)
        result = self.conn.execute(query).fetchall()
        return len(result) == 1

    def component_exists(self, component):
        """Checks if a user is in the database

        Args:
            component (string): Component string

        Returns:
            boolean: Whether component exists in the database
        """
        query = select(self.components_table.c.component).where(
            self.components_table.c.component == component)
        result = self.conn.execute(query).fetchall()
        return len(result) > 1
