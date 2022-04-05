import sqlite3
import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Query, declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
con = sqlite3.connect('database.db')
Base = declarative_base()
cur = con.cursor()
saltrounds = 16
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class Database:
    def add_user(username, password):
        salt = bcrypt.gensalt(rounds=saltrounds)
        hashed = bcrypt.hashpw(password, salt)

        user = User(username=username, password=hashed)
        session.add(user)
        print(user.id)

        user_in_db = session.query(User).filter_by(username=username)

    def verify_password(username, password):
        pass

    def remove_user(id):
        pass

    def add_component(component, id):
        pass

    def remove_component(component):
        pass
