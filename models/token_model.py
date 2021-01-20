from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from settings import app


db = SQLAlchemy(app)

class Token(db.Model):
    __tablename__ = "gs_token"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    token_value = db.Column(db.String(512), nullable = False)
    issued_at = db.Column(db.DateTime, nullable = False, default = datetime.now())
    
    def get_token_by_user(user_id):
        return Token.query.filter_by(user_id = user_id).first()
    
    def create_new_token(user_id, token_value):
        try:
            token = Token(
                user_id = user_id,
                token_value = token_value
            )
            db.session.add(token)
            db.session.commit()
            return token_value
        except Exception as e:
            print(e)
            return False
    
    def validate_token(token_value):
        return Token.query.filter_by(token_value = token_value).first()

    def refresh_token(token, token_value):
        try:
            token.token_value = token_value
            token.issued_at = datetime.now()
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

try:
    db.create_all()
except Exception as e:
    print(e)
    