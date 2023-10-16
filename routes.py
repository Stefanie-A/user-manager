from app import *
from flask import Flask, request, jsonify

#Signup endpoint
@app.route("/home/sign-up/", methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if username is None or email is None or password is None or confirm_password is None:
        return jsonify({"message": "Please fill in required fields"})
    
    user = Users(
        username = username,
        email = email,
        password = password,
        confirm_password = confirm_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User successfully created"})