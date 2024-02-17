from datetime import datetime
from controller.post_controller import *
from controller.user_controller import *
from model.da import *
from model.da.comment_da import *
from model.entity import *
from model.entity.comment import Comment
from tools.Validator import *

class CommentController:
    current_comment = None
    @classmethod
    def save(cls, text, post, user):
        try:
            if text_validator(text) and verify_user_for_comment(user) and verify_post_for_comment(post):
                comment = Comment(text, post, user)
                da = CommentDa()
                da.save(comment)
                return "Saved"
            else:
                raise ValueError
        except ValueError as e:
            return str(e)

    @classmethod
    def edit(cls, id, text, post, user):
        try:
            if comment_id_validator(id) and text_validator(text) and verify_user_for_comment(user) and verify_post_for_comment(post):
                da = CommentDa()
                comment = da.find_by_id_internal(Comment, id)
                comment.post = post
                comment.user = user
                comment.text = text
                comment.date_time = datetime.now()
                da.edit(comment)
                return "Edited"
            else:
                raise ValueError
        except ValueError as e:
            return str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = CommentDa()
            if da.find_by_id(Comment, id):
                da.remove_by_id(Comment, id)
                return "Removed"
            else:
                raise ValueError("Comment Doesnt Exist!!!")
        except Exception as e:
            return str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CommentDa()
            return da.find_all(Comment)
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = CommentDa()
            if da.find_by_id(Comment, id):
                return da.find_by_id(Comment, id)
            else:
                raise ValueError("Comment Doesnt Exist")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_id_internal(cls, id):
        try:
            da = CommentDa()
            if da.find_by_id_internal(Comment, id):
                return da.find_by_id_internal(Comment, id)
            else:
                raise ValueError("Comment Doesnt Exist")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_user(cls, user):
        try:
            if verify_user_for_comment(user):
                da = CommentDa()
                if da.find_by_user(Comment, user):
                    return da.find_by_user(Comment, user)
                else:
                    raise ValueError("This User has no comment!!!")
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_post(cls, post):
        try:
            da = CommentDa()
            if verify_post_for_comment(post):
                if da.find_by_post(Comment, post):
                    return da.find_by_post(Comment, post)
                else:
                    raise ValueError("There is no Comment on this Post")
            else:
                raise ValueError("Post Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    @classmethod
    def find_by_text(cls, text):
        try:
            da = CommentDa()
            if da.find_by_text(Comment, text):
                return da.find_by_text(Comment, text)
            else:
                raise ValueError("No Comment Found")
        except Exception as e:
            return str(e)


    def get_comments_sorted_by_date_and_post_id(self):
        da = CommentDa()
        comments = da.find_all(Comment)
        sorted_comments = sorted(comments, key=lambda comment: (-comment.id) and (-comment.post_id))
        return sorted_comments