from model.entity import *
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Like(Base):
    __tablename__ = "like_tbl"
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable="True")
    user = relationship("User")

    post_id = Column(Integer, ForeignKey("post_tbl.id"), nullable="True")
    post = relationship("Post")

    def __init__(self, post, user):
        self.post = post
        self.user = user
        self.date_time = datetime.now()
