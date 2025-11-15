from dao.user_dao import UserDAO

class UserProvider:

    @staticmethod
    def create_user_pr(data):
        name = data.get("name")
        email = data.get("email")
        return UserDAO.create_user(name, email)

    @staticmethod
    def get_users_pr():
        return UserDAO.get_all_users()
    
    @staticmethod
    def get_user_pr(user_id):
        return UserDAO.get_user_by_id(user_id)
    
    @staticmethod
    def update_user_pr(user_id, data):
        name = data.get("name")
        email = data.get("email")
        return UserDAO.update_user(user_id, name, email)

    @staticmethod
    def delete_user_pr(user_id):
        return UserDAO.delete_user(user_id)
    