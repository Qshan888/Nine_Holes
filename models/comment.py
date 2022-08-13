# ! Creating a new comment model.
from app import db
from models.base import BaseModel


class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    golf_id = db.Column(db.Integer, db.ForeignKey('golfs.id', ondelete='CASCADE'), nullable=False)

    # user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    # user = db.relationship('UserModel', backref='comment_users')