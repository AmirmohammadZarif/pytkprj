from model.da.user_da import *
from tools.Validator import *
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment


class UserController:
    current_user = None
    @classmethod
    def save(cls, name, family, username, password, status=True):
        try:
            if name_validator(name) and name_validator(family) and username_validator(username):
                user = User(name, family, username, password, status=True)
                da = UserDa()
                da.save(user)
                return "Saved"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return str(e)
    @classmethod
    def edit(cls, id, name, family, username, password, status):
        try:
            if name_validator(name) and name_validator(family) and user_id_validator(id):
                da = UserDa()
                user = da.find_by_id(User, id)
                user.name = name
                user.family = family
                user.username = username
                user.password = password
                user.status = status
                da.edit(user)
                return "Edited"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return str(e)
    @classmethod
    def remove(cls, id):
        try:
            if user_id_validator(id):
                da = UserDa()
                da.remove_by_id(User, id)
                return "Removed"
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)
    @classmethod
    def find_all(cls):
        try:
            da = UserDa()
            return da.find_all(User)
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = UserDa()
            if da.find_by_id(User, id):
                return da.find_by_id(User, id)
            else:
                raise ValueError("User Doesnt Exist")
        except Exception as e:
            return str(e)
    @classmethod
    def find_by_id_internal(cls, id):
        try:
            da = UserDa()
            if da.find_by_id_internal(User, id):
                return da.find_by_id_internal(User, id)
            else:
                raise ValueError("User Doesnt Exist")
        except Exception as e:
            return str(e)
    @classmethod
    def find_by_username(cls, username):
        try:
            da = UserDa()
            if da.find_by_username(User, username):
                return da.find_by_username(User, username)
            else:
                raise ValueError("Username Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            da = UserDa()
            if da.find_by_username_and_password(username, password):
                return da.find_by_username_and_password(username, password), None
            else:
                return None, "Username or Password Doesn't Exist!!!"
        except Exception as e:
            return None, str(e)
