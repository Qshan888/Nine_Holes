
from app import db
from models.base import BaseModel
from models.category import CategoryModel
from models.comment import CommentModel
from models.golf_category import golf_category


class GolfModel(db.Model, BaseModel):

  __tablename__ = "golfs"

  name = db.Column(db.Text, nullable=False, unique=True)
  image = db.Column(db.Text, nullable=False)
  product_type_code = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  in_stock = db.Column(db.Boolean, nullable=False)
  rating = db.Column(db.Float, nullable=False)
  location = db.Column(db.Text, nullable=False)


  comments = db.relationship('CommentModel', backref='comments', cascade="all, delete")
  categories = db.relationship('CategoryModel', backref='categories', secondary=golf_category)

#   categories = db.relationship('GolfCategoryModel', back_populates="golf")
#   comments = db.relationship('CommentModel', backref='golfs', cascade="all, delete")

