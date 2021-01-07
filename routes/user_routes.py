from responses.standard_response_body import StandardResponseBody
from flask import request, jsonify
from controllers import user_controller
import json

def create_user():
    data = json.loads(request.data)
    #print(data)
    if 'name' not in data:
        return jsonify(StandardResponseBody('Error', "'name' is a required field").to_dict()), 400
    elif 'email' not in data:
        return jsonify(StandardResponseBody('Error', "'email' is a required field").to_dict()), 400
    elif 'username' not in data:
        return jsonify(StandardResponseBody('Error', "'username' is a required field").to_dict()), 400
    elif 'password' not in data:
        return jsonify(StandardResponseBody('Error', "'password' is a required field").to_dict()), 400

    name = data['name']
    email = data['email']
    username = data['username']
    password = data['password']

    return user_controller.create_user(name, email, username, password)