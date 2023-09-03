from config import session_scope
from models.user import User, format_user
from flask import request, Blueprint

usersAPI = Blueprint("usersAPI", __name__)

# Create a user
@usersAPI.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    user = User(
        username=username
    )
    with session_scope() as db_session:
        db_session.add(user)
    return format_user(user), 201

# Get all users
@usersAPI.route('/users/', methods=['GET'])
def get_users():
    with session_scope() as db_session:
        users = db_session.query(User).all()
        users_list = [format_user(user) for user in users]
    return users_list, 200

# Get a specific user
@usersAPI.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    with session_scope() as db_session:
        user = db_session.query(User).filter(User.username == username)[0]
    return format_user(user), 200

# Delete a specific user
@usersAPI.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    with session_scope() as db_session:
        user = db_session.query(User).filter(User.username == username)[0]
        db_session.delete(user)
    return format_user(user), 200