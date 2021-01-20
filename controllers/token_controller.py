from responses.standard_response_body import StandardResponseBody
from responses.login_response_body import LoginResponseBody
from datetime import datetime, timedelta
from models.token_model import Token
from flask import jsonify
from settings import app
import secrets


validity = timedelta(seconds = app.config["TOKEN_VALIDITY_SECONDS"])

def generate_token():
    gen = secrets.token_hex(32)
    while Token.validate_token(gen):
        gen = secrets.token_hex(32)
    return gen

def check_token_timeout(token):
    return (token.issued_at + validity) > datetime.now()

def get_token_by_user(user):
    ''' check in token db '''
    token = Token.get_token_by_user(user.id)
    if token == None:
        ''' create new token '''
        token_value = generate_token()
        return Token.create_new_token(user.id, token_value)        
    else:
        ''' check if token valid '''
        if check_token_timeout(token):
            ''' return token value '''
            return token.token_value
        else:
            ''' update token '''
            return update_token(token.token_value)

def update_token(token_value):
    token = Token.validate_token(token_value)
    if token != None:
        token_value = generate_token()
        if Token.refresh_token(token, token_value):
            return token_value
    return False

def validate_token(token_value):
    token = Token.validate_token(token_value)
    if token != None:
        if check_token_timeout(token):
            return jsonify(LoginResponseBody("Success", "Token valid", token.token_value).to_dict()), 200
    return jsonify(StandardResponseBody("Unauthorized", "Token invalid or expired").to_dict()), 401