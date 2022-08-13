from app import db
# from models.base import BaseModel

golf_category = db.Table('golfs_categories',
    db.Column('golf_id', db.Integer, db.ForeignKey('golfs.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

# class GolfCategoryModel(db.Model, BaseModel):


#     golf_id = db.Column(db.Integer, db.ForeignKey("golfs.id", primary_key=True)
#     category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), primary_key=True)
#     # quantity = db.Column(db.Integer())

#     # golf = db.relationship("GolfModel", back_populates="categories")
#     # category = db.relationship("CategoryModel", back_populates="golfs")
