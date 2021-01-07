from responses.standard_response_body import StandardResponseBody
from models.user_model import User
from flask import jsonify


def create_user(name, email, username, password):
    e = User.find_by_email(email)
    if e > 0:
        return jsonify(StandardResponseBody('Error', 'Email already exists').to_dict())

    username_count = User.get_username_count(username)
    #print(username_count)

    if User.create_new_user(name, email, username, password, username_count):
        return jsonify(StandardResponseBody('Success', 'Successfully created user').to_dict())
    else:
        return jsonify(StandardResponseBody('Error', 'Failed to create user').to_dict())