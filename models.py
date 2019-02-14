from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email=Column(String(512))
    full_name=Column(String(512))
    password=Column(String(512))
    is_admin=Column(Boolean(), default=False)
    last_login=Column(DateTime(), nullable=True)

    @staticmethod
    def find_by_id(id_value):
        return 
        db.session.query(User).filter(User.user_id == id_value).one()

    @staticmethod
    def find_by_email(email):
        return
        db.session.query(User).filter(User.email == email).one()

    @staticmethod
    def all():
        return list(db.session.query(User).all())

def create_user(email, full_name, password, is_admin=False):
    new_user=User()
    new_user.email=email
    new_user.full_name=full_name
    new_user.password=password
    new_user.is_admin=is_admin
    db.session.add(new_user)
    db.session.commit()
    return new_user

