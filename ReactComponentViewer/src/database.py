"""Module for database actions"""
import numpy as np
import bcrypt
from sqlalchemy import (Column, Table, Integer, String,
                        MetaData, inspect, create_engine, select, insert, update)

SALTROUNDS = 10


class Database:
    """ Database is responsible for creating users and components to
        the database as well as removing them."""

    def __init__(self):
        print('creating connnection')
        self.engine = create_engine(
            'sqlite:///database.db', echo=False)
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
        """Adds auser to database"""
        salt = bcrypt.gensalt(rounds=SALTROUNDS)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)
        pw_hash = hashed.decode('utf8')

        ins = insert(self.users_table).values(
            username=username, password=pw_hash)
        self.engine.execute(ins)

    def verify_password(self, username, password):
        """Verifies user password"""
        users_table = self.users_table

        query = select(users_table.c.password).where(
            users_table.c.username == username)
        hashed = self.conn.execute(query).fetchone()
        print()
        print()
        print()
        print(hashed)
        if len(hashed) > 0:
            is_auth = bcrypt.checkpw(password.encode(
                'utf8'), hashed[0].encode('utf8'))
            return is_auth
        return False

    def save_component(self, name, owner_id, component):
        """Saves a component to the database"""
        ins = insert(self.components_table).values(
            component=component, name=name, owner_id=owner_id)
        self.engine.execute(ins)

    # def remove_user(self, user_id):
    #     """Removes user from database"""
    #     pass

    # def remove_component(self, component_id):
    #     """Removes a component from database"""
    #     pass

    def get_components_for_user(self, username):
        """Gets a users components"""
        user_id = self.get_user_id(
            username)  # pylint: disable=no-value-for-parameter
        components_table = self.components_table
        query = select(components_table.c.component).where(
            components_table.c.owner_id == user_id)
        components = self.conn.execute(query).fetchall()
        return self.row_as_array(components)

    def get_user_id(self, username):
        """Gets a users id by their username"""
        query = select(self.users_table.c.id).where(
            self.users_table.c.username == username)
        result = self.conn.execute(query).fetchone()
        if len(result) > 0:
            return result[0]
        return 0

    def get_user_components(self, user_id):
        """Gets a users components"""
        query = select(self.components_table.c.name, self.components_table.c.component,
                       self.components_table.c.id).where(
            self.components_table.c.owner_id == user_id)
        result = self.conn.execute(query).fetchall()

        return row_as_array(result)

    def patch_component(self, component_id, new_component):
        """Updates a component"""
        query = (
            update(self.components_table).
            where(self.components_table.c.id == component_id).
            values(component=new_component)
        )
        print(query)
        self.conn.execute(query)
        print('updated in database')

    def get_community_components(self):
        """Loads the community components"""
        query = select(self.components_table.c.name, self.components_table.c.component,
                       self.components_table.c.id)
        result = self.conn.execute(query).fetchall()
        return row_as_array(result)


def row_as_array(rows):
    """LegacyRow as an array. This gives the row mutability."""
    new_arr = []
    for row in rows:
        new_arr.append(np.asarray(row).tolist())
    return new_arr
