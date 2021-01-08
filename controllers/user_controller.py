from responses.standard_response_body import StandardResponseBody
from models.user_model import User
from flask import jsonify
import bcrypt


def hash_password(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def check_password(password, hashed):
    print(bcrypt.checkpw(password, hashed))
    return True


def create_user(name, email, username, password):
    e = User.find_by_email(email)
    #print(e)
    if e != None:
        return jsonify(StandardResponseBody('Error', 'Email already exists').to_dict())

    username_count = User.get_username_count(username)
    password = hash_password(password.encode("utf-8")).decode("utf-8")

    #print(password)
    if User.create_new_user(name, email, username, password, username_count):
        return jsonify(StandardResponseBody('Success', 'Successfully created user').to_dict())
    else:
        return jsonify(StandardResponseBody('Error', 'Failed to create user').to_dict())

def sign_in(email, password):
    user = User.find_by_email(email)
    if user != None:
        if check_password(password.encode("utf-8"), user.password.encode("utf-8")):
            return jsonify(StandardResponseBody('Success', 'Successfully logged in').to_dict())
        else:
            return jsonify(StandardResponseBody('Error', 'Invalid email or password').to_dict())
    return jsonify(StandardResponseBody('Error', 'Invalid email or password').to_dict())