from models.user_model import User
from extensions.db import db


class UserDAO:
    @staticmethod
    def create_user(name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, name, email):
        user = UserDAO.get_user_by_id(user_id)
        user.name = name
        user.email = email
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        db.session.delete(user)
        db.session.commit()
        return True


