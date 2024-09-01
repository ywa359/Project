from flask import Blueprint, request, jsonify

from data_model.http_response import *
from data_model.user import User
from utils.db_session import db_session

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json

    # Check if the request data is valid
    if not data or not data.get('username') or not data.get('password'):
        return jsonify(
            NotFoundResponse('Username and password are required').to_dict())

    username = data.get('username')
    password = data.get('password')

    # Query for the user by username4
    # select * from user where user_name=%s limit 1
    # [User]
    user = db_session.query(User).filter(User.user_name == username).first()

    # Verify the password
    if user and (user.password == password):
        return jsonify(
            HTTPResponse(200, "Welcome Back %s" % (user.user_name),
                         user.id).to_dict()
        )
    else:
        return jsonify(
            NotFoundResponse('Invalid username or password').to_dict())


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = db_session.query(User).filter(
        (User.user_name == username)).first()
    if user is not None:
        return jsonify(SuccessResponse(
            "This account already exists, please turn to 'login'").to_dict())
    else:
        user = User(user_name=username, password=password)
        db_session.add(user)
        db_session.commit()
        return jsonify(
            NotFoundResponse('Register success').to_dict())
