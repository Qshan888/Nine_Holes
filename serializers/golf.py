from app import ma
from models.golf import GolfModel
from marshmallow import fields

# ! Care with the casing here.
# ! Extending the marshmallow serializer schema
# ? A schema says how to serialize:
# Python Model -> JSON
# Python Dictionary -> Python Model


class GolfSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = GolfModel

        load_instance = True

    comments = fields.Nested("CommentSchema", many=True)
    categories = fields.Nested("CategorySchema", many=True)
    user = fields.Nested("UserSchema", many=False)