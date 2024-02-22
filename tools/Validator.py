import re
from model.da.database_manager import DatabaseManager
from model.entity.user import User
from model.entity.post import Post
from model.entity.like import Like
from model.entity.comment import Comment


def name_validator(x):
    return bool(re.match("^[A-Za-z\s]{2,20}$", x, re.I))


def username_validator(x):
    db = DatabaseManager()
    if not db.find_by_username(User, x):
        return True
    else:
        raise ValueError("Duplicate Username")


def text_validator(x):
    if len(x) < 30:
        return True
    else:
        raise ValueError("Text Too Long!!")


def text_validator(x):
    if len(x) < 30:
        return True
    else:
        raise ValueError("Text Too Long!!")

def post_id_validator(x):
    db = DatabaseManager()
    if db.find_by_id_internal(Post, x):
        return True
    else:
        raise ValueError("Post Doesn't Exist!!!")


def user_id_validator(x):
    try:
        db = DatabaseManager()
        if db.find_by_id_internal(User, x):
            return db.find_by_id_internal(User, x)
        else:
            raise ValueError("User Doesnt Exist")
    except:
        raise ValueError("User Doesnt Exist")


def verify_user_for_post(user):
    if (user is None) or (not isinstance(user, User)):
        raise ValueError("User does not exist.")
    db = DatabaseManager()
    verified_user = db.find_by_id_internal(User, user.id)
    if verified_user is None:
        raise ValueError("User does not exist.")
    else:
        return verified_user


def verify_user_for_comment(user):
    if (user is None) or (not isinstance(user, User)):
        raise ValueError("User does not exist.")
    db = DatabaseManager()
    verified_user = db.find_by_id_internal(User, user.id)
    if verified_user is None:
        raise ValueError("User does not exist.")
    else:
        return verified_user


def verify_post_for_comment(post):
    if (post is None) or (not isinstance(post, Post)):
        raise ValueError("Post does not exist.")
    db = DatabaseManager()
    verified_post = db.find_by_id_internal(Post, post.id)
    if verified_post is None:
        raise ValueError("Post does not exist.")
    else:
        return verified_post


def comment_id_validator(x):
    try:
        db = DatabaseManager()
        if db.find_by_id_internal(Comment, x):
            return db.find_by_id_internal(Comment, x)
        else:
            raise ValueError("Comment Doesnt Exist")
    except:
        raise ValueError("Comment Doesnt Exist")
