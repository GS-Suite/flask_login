from settings import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), primary_key = True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(512),nullable = False)
    created = db.Column(db.DateTime, nullable = False)
    username_count = db.Column(db.Integer, nullable = False)

    def create_new_user(name, email, username, password, username_count):
        try:
            new_user = User(
                name = name,
                email = email,
                username = username,
                password = password,
                created = datetime.now(),
                username_count = username_count
            )
            db.session.add(new_user)
            db.session.commit()
            print("created")
            return True
        except Exception as e:
            print(e)
            return False
    
    def find_by_email(email):
        email_count = User.query.filter_by(email = email).count()
        return email_count
    
    def get_username_count(username):
        count = User.query.filter_by(username = username).all()
        x = len(count)
        print(x, count.count)
        return x
    
    