"""
Users endpoint
"""

from flask import Blueprint, request
from my_api.endpoints.models import add_user

# Create the users blueprint
USERS = Blueprint('users', __name__)


@USERS.route('/register', methods=['POST'])
def user_register():
    data = request.get_json()
    if add_user(data['username'], data['password']):
        return "User added successfully."

    


@USERS.route('/login', methods=['POST'])
def user_login():
    """
    This method handles user login
    """
    pass


@USERS.route('/logout', methods=['POST'])
def user_logout():
    """
    This method handles user logout
    """
    pass
