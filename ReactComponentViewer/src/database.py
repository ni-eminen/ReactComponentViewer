"""Module for database actions"""
import bcrypt
from sqlalchemy import (Column, Table, Integer, String,
                        MetaData, inspect, create_engine, select, insert)

SALTROUNDS = 10


class Database:
    """ Database is responsible for creating users and components to
        the database as well as removing them."""

    def __init__(self):
        print('creating connnection')
        self.engine = create_engine('sqlite:///database.db', echo=False)
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
                Column('component', String)
            )

        meta.reflect()
        self.users_table = meta.tables['users']
        self.components_table = meta.tables['components']

        meta.create_all(self.engine)

    def add_user(self, username, password):
        """Adds auser to database"""
        salt = bcrypt.gensalt(rounds=SALTROUNDS)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        ins = insert(self.users_table).values(
            username=username, password=hashed)
        self.engine.execute(ins)

    def verify_password(self, username, password):
        """Verifies user password"""
        users_table = self.users_table

        query = select(users_table.c.password).where(
            users_table.c.username == username)
        hashed = self.conn.execute(query).fetchone()
        if len(hashed) > 0:
            is_auth = bcrypt.checkpw(password.encode('utf8'), hashed[0])
            return is_auth
        return False

    # def remove_user(self, user_id):
    #     """Removes user from database"""
    #     pass

    # def add_component(self, component, user_id):
    #     """Adds a component to database"""
    #     pass

    # def remove_component(self, component_id):
    #     """Removes a component from database"""
    #     pass


def get_components_for_user(self, username):
    """Gets a users components"""
    user_id = get_user_id(username)  # pylint: disable=no-value-for-parameter
    components_table = self.components_table
    query = select(components_table.c.component).where(
        components_table.c.owner_id == user_id)
    components = self.conn.execute(query).fetchall()
    return components


def get_user_id(self, username):
    """Gets a users id by their username"""
    query = select(self.users_table.c.id).where(
        self.users_table.c.username == username)
    result = self.conn.execute(query).fetchone()
    if len(result) > 0:
        return result[0]
    return 0
