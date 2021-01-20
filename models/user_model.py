from settings import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "gs_user"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(512),nullable = False)
    name = db.Column(db.String(50), nullable = False)
    username_count = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False)

    def create_new_user(name, email, username, password, username_count):
        try:
            new_user = User(
                email = email,
                username = username,
                password = password,
                name = name,
                username_count = username_count,
                created_at = datetime.now()
            )
            db.session.add(new_user)
            db.session.commit()
            #print("created")
            return True
        except Exception as e:
            print(e)
            return False
    
    def find_by_email(email):
        user = User.query.filter_by(email = email).first()
        return user
    
    def get_username_count(username):
        count = User.query.filter_by(username = username).all()
        x = len(count)
        print(x, count.count)
        return x

try:
    db.create_all()
except Exception as e:
    print(e)