from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from model.entity.base import Base
from sqlalchemy import and_
from model.entity import *


class DatabaseManager:
    def __init__(self):
        self.engine = None
        self.session_factory = None
        self.session = None

    def make_engine(self):
        if not database_exists("mysql+pymysql://root@localhost:3306/mft"):
            create_database("mysql+pymysql://root@localhost:3306/mft")
        if not self.engine:
            self.engine = create_engine("mysql+pymysql://root@localhost:3306/mft")
            Base.metadata.create_all(self.engine)
            self.session_factory = sessionmaker(bind=self.engine)
        if not self.session:
            self.session = scoped_session(self.session_factory)

    def save(self, entity):
        self.make_engine()
        # self.session.add(entity)
        local = self.session.merge(entity)
        self.session.add(local)
        self.session.commit()
        return entity

    def edit(self, entity):
        self.make_engine()
        local = self.session.merge(entity)
        self.session.add(local)
        self.session.commit()
        return entity


    def remove(self, entity):
        self.make_engine()
        try:
            self.session.delete(entity)
            self.session.commit()
        except Exception as e:
            raise e

    def remove_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        if entity:
            try:
                self.session.delete(entity)
                self.session.commit()
            except Exception as e:
                str(e)

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        return entity_list

    def find_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        return entity

    def find_by_username(self, class_name, username):
        self.make_engine()
        result = self.session.query(class_name).filter(class_name.username == username).all()
        return result

    def find_by_id_internal(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        self.session.close()
        return entity

    def find_by_user(self, class_name, user):
        self.make_engine()
        result = self.session.query(class_name).filter(class_name.user == user).one()
        return result

    def find_by_text(self, class_name, text):
        self.make_engine()
        result = self.session.query(class_name).filter(class_name.text == text).all()
        return result

    def find_by_post(self, class_name, post):
        self.make_engine()
        result = self.session.query(class_name).filter(class_name.post == post).all()
        return result
