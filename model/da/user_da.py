from model.da.database_manager import *
from model.entity import *

class UserDa(DatabaseManager):
    def find_by_username_and_password(self, username, password):
        try:
            self.make_engine()
            result = self.session.query(User).filter(and_(User.username == username, User.password == password)).one()
            return result
        except Exception as e:
            raise ValueError("Username and/or Password doesnt Exist")
