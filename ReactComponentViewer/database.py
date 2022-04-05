import bcrypt
from sqlalchemy import Column, Integer, String, Table, Column, Integer, String, MetaData, inspect, create_engine, select, insert

saltrounds = 10


class Database:
    """Database is responsible for creating users and components to the database as well as removing them."""

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
        salt = bcrypt.gensalt(rounds=saltrounds)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        ins = insert(self.users_table).values(
            username=username, password=hashed)

    def verify_password(self, username, password):
        users_table = self.users_table
        try:
            s = select(users_table.c.password).where(
                users_table.c.username == username)
            hashed = self.conn.execute(s).fetchone()[0]
            isAuth = bcrypt.checkpw(password.encode('utf8'), hashed)
            return isAuth
        except Exception as e:
            print('exception in verify_password:', str(e))

    def remove_user(id):
        pass

    def add_component(component, id):
        pass

    def remove_component(component):
        pass


def get_components_for_user(self, username):
    id = get_user_id(username)
    components_table = self.components_table
    s = select(components_table.c.component).where(
        components_table.c.owner_id == id)
    components = self.conn.execute(s).fetchall()
    return components


def get_user_id(self, username):
    s = select(self.users_table.c.id).where(
        self.users_table.c.username == username)
    try:
        result = self.conn.execute(s).fetchone()[0]
        return result
    except Exception as e:
        print('exception in get_user_id:', str(e))
