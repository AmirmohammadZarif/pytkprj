from datetime import datetime
from model.da.user_da import UserDa
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like
from model.da.post_da import *
from tools.Validator import text_validator, post_id_validator, user_id_validator, verify_user_for_post


class PostController:
    current_post=None
    @classmethod
    def save(cls, text, user):
        try:
            if (verify_user_for_post(user)) and (text_validator(text)):
                da = PostDa()
                print(text)
                user = da.find_by_id_internal(User, user.id)
                post = Post(text, user)
                da.save(post)
                return "Saved"
            else:
                return ValueError
        except ValueError as e:
            return str(e)
    @classmethod
    def edit(cls, id, text, user):
        try:
            if text_validator(text) and verify_user_for_post(user) and post_id_validator(id):
                da = PostDa()
                post = da.find_by_id_internal(Post, id)
                post.user = user
                post.text = text
                post.date_time = datetime.now()
                da.edit(post)
                return "Edited"
            else:
                raise ValueError
        except ValueError as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                if da.find_by_id(Post, id):
                    da.remove_by_id(Post, id)
                    return "Removed"
            else:
                raise ValueError
        except Exception as e:
            return str(e)

    @classmethod
    def find_all(cls):
        try:
            da = PostDa()
            return da.find_all(Post)
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                return da.find_by_id(Post, id)
            else:
                raise ValueError("Post Doesnt Exist")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id_internal(cls, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                return da.find_by_id_internal(Post, id)
            else:
                raise ValueError("Post Doesnt Exist")
        except Exception as e:
            return str(e)
    @classmethod
    def find_by_user(cls, user):
        try:
            if verify_user_for_post(user):
                da = PostDa()
                if da.find_by_user(Post, user):
                    return da.find_by_user(Post, user)
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)
    @classmethod
    def find_by_text(cls, text):
        try:
            da = PostDa()
            if da.find_by_text(Post, text):
                return da.find_by_text(Post, text)
            else:
                raise ValueError("No such a post Exist!!!")
        except Exception as e:
            return str(e)
