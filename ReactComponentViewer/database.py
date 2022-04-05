import sqlite3
import bcrypt
from sqlalchemy import Column, Integer, String, Table, Column, Integer, String, MetaData, inspect, create_engine, select
from sqlalchemy.orm import Query, declarative_base, sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
conn = engine.connect()
saltrounds = 16
meta = MetaData(bind=engine)

if not inspect(engine).has_table('users'):
    users_table = Table(
        'users', meta,
        Column('id', Integer, primary_key=True),
        Column('username', String),
        Column('password', String),
    )
if not inspect(engine).has_table('components'):
    components = Table(
        'components', meta,
        Column('id', Integer, primary_key=True),
        Column('owner_id', Integer),
        Column('component', String)
    )

meta.reflect()
users_table = meta.tables['users']
components_table = meta.tables['components']

meta.create_all(engine)


class Database:
    """Database is responsible for creating users and components to the database as well as removing them."""
    def add_user(username, password):
        salt = bcrypt.gensalt(rounds=saltrounds)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        print(username)
        print(hashed)

        ins = users_table.insert().values(username=username, password=hashed)
        conn.execute(ins)
        # cur.execute(f"insert into users (username, password) values ('{username}', '{hashed}');")

    def verify_password(username, password):
        try:
            s = select(users_table.c.password).where(
                users_table.c.username == username)
            hashed = conn.execute(s).fetchone()[0]
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
