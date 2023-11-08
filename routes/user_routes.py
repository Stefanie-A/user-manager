from flask import request, jsonify, Blueprint
from models.user import Users
import re
from database import db


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

    return jsonify({"message": "User successfully created"}), 200

#login endpoint
@user_bp.route("/home/login/", methods=['GET'])
def sign_in():
    users = Users.query.all()
    users_login = [ ]
    for user in users:
        users_login.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password': user.password
        })
    return jsonify(users_login)
    
#update endpoint
@user_bp.route("/home/login/update/<user_id>/", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    users = Users.query.get(user_id)

    if not users:
        return jsonify ({
            'error': "User not found"
        }), 401
    
    users.username = data.get('username', users.username),
    users.email = data.get('email', users.email),
    users.password = data.get('password', users.password)

    db.session.add(users)
    db.session.commit()

#delete endpoint
@user_bp.route("/home/login/delete/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 401
    try:
        db.session.delete(user_id)
        db.session.commit()
        return jsonify({"message": "User successfully deleted"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    



# Issues: this code code won't work right now due to circular import.