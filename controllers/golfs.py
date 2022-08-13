from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from models.golf import GolfModel
from models.category import CategoryModel
from models.comment import 	CommentModel

from serializers.golf import GolfSchema
from serializers.comment import CommentSchema


from middleware.secure_route import secure_route

golf_schema = GolfSchema()
comment_schema = CommentSchema()

router = Blueprint("golfs", __name__)


@router.route("/golfs", methods=["GET"])
def get_golfs():
	golfs = GolfModel.query.all()

	return golf_schema.jsonify(golfs, many=True), HTTPStatus.OK


@router.route("/golfs/<int:golf_id>", methods=["GET"])
def get_single_golf(golf_id):

    golf = GolfModel.query.get(golf_id)

    if not golf:
      return { "message": "Golf not found" }, HTTPStatus.NOT_FOUND

    return golf_schema.jsonify(golf), HTTPStatus.OK

@router.route("golfs", methods=["POST"])
def create_golf():
	golf_dictionary = request.json

	try:
		golf = golf_schema.load(golf_dictionary)

	except ValidationError as e:
		return { "error": e.messages, "message": "Something went wrong" }, HTTPStatus.NOT_FOUND

	golf.save()

	return golf_schema.jsonify(golf), HTTPStatus.OK



@router.route("/golfs/<int:golf_id>", methods=["PUT"])
def update_golf(golf_id):
    golf_dictionary = request.json
    existing_golf = GolfModel.query.get(golf_id)

    if not existing_golf:
        return {"message": "Golfclub not found"}, HTTPStatus.NOT_FOUND

    try:
        golf = golf_schema.load(golf_dictionary, instance=existing_golf, partial=True)

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    golf.save()

    return golf_schema.jsonify(golf), HTTPStatus.OK


@router.route("/golfs/<int:golf_id>", methods=["DELETE"])
def remove_golf(golf_id):
    golf = GolfModel.query.get(golf_id)

    if not golf:
        return {"message": "Golfclub not found"}, HTTPStatus.NOT_FOUND

    golf.remove()

    return '', HTTPStatus.NO_CONTENT



@router.route('/golfs/<int:golf_id>/comments', methods=['POST'])
@secure_route
def create_comment(golf_id):

  comment_dictionary = request.json
  print(comment_dictionary)

  try:
    comment = comment_schema.load(comment_dictionary)

  except ValidationError as e:
    return { "errors": e.messages, "message": "Something went wrong" }

  comment.golf_id = golf_id
  comment.save()
  print(comment)

  return comment_schema.jsonify(comment), HTTPStatus.OK


@router.route("/golfs/<int:golf_id>/comments/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(golf_id, comment_id):

    comment_dictionary = request.json
    existing_comment = CommentModel.query.get(comment_id)

    if not existing_comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    try:
        comment = comment_schema.load(
            comment_dictionary, # ! All the fields you're changing
            instance=existing_comment, # ! Existing comment you're updating
            partial=True # ! This allows you to ONLY provide the fields you're changing.
        )

    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    comment.save()

    golf = GolfModel.query.get(golf_id)

    if not golf:
        return {"message": "Golf not found"}, HTTPStatus.NOT_FOUND

    return golf_schema.jsonify(golf), HTTPStatus.OK


@router.route("/golfs/<int:golf_id>/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(golf_id, comment_id):

    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    comment.remove()

    golf = GolfModel.query.get(golf_id)

    if not golf:
        return {"message": "Golf not found"}, HTTPStatus.NOT_FOUND

    return golf_schema.jsonify(golf), HTTPStatus.OK


@router.route("/golfs/<int:golf_id>/categories/<int:category_id>", methods=["POST"])
@secure_route
def create_fruit_falvour(golf_id, category_id):
    # ! This assumes both the note and the tea exists.

    golf = GolfModel.query.get(golf_id)

    category = CategoryModel.query.get(category_id)

    if not category or not golf:
        return {"message": "Item not found"}, HTTPStatus.NOT_FOUND

    # ! This is possible cuz of the relationship field in TeaModel
    # ! Add the note to the tea. This defines the relationship.
    golf.category.append(category)

    golf.save()

    return golf_schema.jsonify(golf), HTTPStatus.OK