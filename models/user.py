from datetime import datetime, timedelta
import jwt

# ! Imported a hybrid_property.
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt
from models.base import BaseModel
from config.environment import secret
# from models.order import OrderModel

class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    password_hash = db.Column(db.Text, nullable=True)

    # order_id = db.Column(db.Integer, db.ForeignKey("order.id", ondelete='CASCADE'), nullable=False)

    # order = db.relationship('OrderModel', backref='orders')


    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        print("inside password hash method")
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode('utf-8')


    def validate_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)

    def generate_token(self):

        payload = {
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": self.id,
        }

        token = jwt.encode(
            payload,
            secret,
            algorithm="HS256",
        )

        return token

