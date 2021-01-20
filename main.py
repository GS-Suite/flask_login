from routes import user_routes, token_routes
from flask_sqlalchemy import SQLAlchemy
from settings import app


@app.route("/sign_up/", methods = ["POST"])
def create_user():
    return user_routes.create_user()

@app.route("/sign_in/", methods = ["POST"])
def sign_in():
    return user_routes.sign_in()

@app.route("/validate_token/", methods = ["POST"])
def validate_token():
    return token_routes.validate_token()

@app.route("/refresh_token/", methods = ["POST"])
def refresh_token():
    return token_routes.refresh_token()


if __name__ == "__main__":
    app.run(debug = False)