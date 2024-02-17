from model.entity import *
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comment_tbl"
    id = Column(Integer, primary_key=True)
    text = Column(String(30))
    date_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable="True")
    user = relationship("User")

    post_id = Column(Integer, ForeignKey("post_tbl.id"), nullable="True")
    post = relationship("Post")

    def __init__(self, text, post, user):
        self.text = text
        self.post = post
        self.user = user
        self.date_time = datetime.now()
    def __repr__(self):
        return str(self.__dict__)