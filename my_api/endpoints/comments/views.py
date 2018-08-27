"""
Comments endpoint
"""
from flask import Blueprint, request, jsonify
from my_api.endpoints.models import (save_comment)


# Create the comments blueprint
COMMENTS = Blueprint('comments', __name__)


@COMMENTS.route('/comments', methods=['POST'])
def create_comment():
    """
    This method handles comment creation
    """
    post_data = request.get_json()
    data = {
        "comment_id":post_data.get("comment_id"),
        "message": post_data.get("message"),
        "author": post_data.get("author"),
        "date created": post_data.get("date_created")
    }
    save_comment(data)
    response_object = {
        "message":data,
        "status": "successfuly posted",
        "msg": "New comment has been successfully added."
    }
    return jsonify(response_object)


@COMMENTS.route('/comments', methods=['GET'])
def get_comment():
    """
    This method allows a user to get their own comment(s)
    """
    pass


@COMMENTS.route('/comments/<comment_id>', methods=['PUT'])
def edit_comment():
    """
    This method allows a user to edit their previous comment
    """
    pass


@COMMENTS.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comment():
    """
    This method allows a moderator to delete a comment
    """
    # Moderator only
    pass
