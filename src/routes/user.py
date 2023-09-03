from config import session_scope
from models.user import User, format_user
from flask import request, Blueprint

usersAPI = Blueprint("usersAPI", __name__)

@usersAPI.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    user = User(
        username=username
    )
    with session_scope() as db_session:
        db_session.add(user)
    return format_user(user), 201
