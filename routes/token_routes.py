from responses.standard_response_body import StandardResponseBody
from responses.login_response_body import LoginResponseBody
from controllers import token_controller
from flask import request, jsonify
import json


def validate_token():
    if 'token' not in request.headers:
        return jsonify(StandardResponseBody('Error', "'token' is a required header").to_dict()), 400

    token_value = request.headers["token"]

    return token_controller.validate_token(token_value)

def refresh_token():
    if "token" not in request.headers:
        return jsonify(StandardResponseBody('Error', "'token' is a required header").to_dict()), 400
    
    token_value = request.headers["token"]
    token = token_controller.update_token(token_value)

    if token:
        return jsonify(LoginResponseBody("Success", "Token updated", token).to_dict()), 200
    else:
        return jsonify(StandardResponseBody("Error", "Unable to update token").to_dict()), 400