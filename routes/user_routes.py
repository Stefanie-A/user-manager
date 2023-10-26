from app import db
from flask import request, jsonify, Blueprint
from models.user import Users
import re
user_bp = Blueprint('user', __name__)

#Signup endpoint
@user_bp.route("/home/sign-up/", methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    pattern = r'^[a-zA-Z-0-9.-]+@+[a-zA-Z-0-9]+\.[a-zA-Z]{3, }$'
    match = re.match(pattern, email)

    if username is None and email is None or (match != email) and password is None:
        return jsonify({"message": "Please fill in required fields and enter a valid email format"})
    
    user = Users(
        username = username,
        email = email,
        password = password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User successfully created"})

#login endpoint
@user_bp.route("/home/login/", methods=['GET'])
def sign_in():
    login = Users.query.all()
    users_login = [ ]
    for users in login:
        users_login.append({
            'id': users.id,
            'username': users.userame,
            'email': users.email,
            'password': users.password
        })
        return jsonify(users_login)
    
#update endpoint
@user_bp.route("/home/login/update/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    login = Users.query.get(user_id)

    if not login:
        return jsonify ({
            'error': "User not found"
        })
    
    login.username = data.get('username', login.username),
    login.email = data.get('email', login.email),
    login.password = data.get('password', login.password)

    db.session.commit()
