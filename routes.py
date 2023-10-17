from app import app, db, Users
from flask import Flask, request, jsonify
import re

#Signup endpoint
@app.route("/home/sign-up/", methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    pattern = r'^[a-zA-Z-0-9.-]+@+[a-zA-Z-0-9]+\.[a-zA-Z]{3, }$'
    match = re.match(pattern, email)

    if username is None or email is None or match is None or password is None:
        return jsonify({"message": "Please fill in required fields and enter a valid email format"})
    
    user = Users(
        username = username,
        email = email,
        password = password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User successfully created"})