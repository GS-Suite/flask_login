from settings import app
from flask_sqlalchemy import SQLAlchemy
from routes import user_routes


@app.route("/sign_up", methods = ["POST"])
def create_user():
    return user_routes.create_user()



if __name__ == "__main__":
    app.run(debug = True)