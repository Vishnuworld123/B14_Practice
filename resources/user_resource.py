from flask_restx import Resource, Namespace, fields
from providers.user_provider import UserProvider

api = Namespace("users", description="User CRUD Operation")

#swagger
user_model = api.model("User", {
    "id": fields.Integer(readOnly=True),
    "name": fields.String(readOnly=True),
    "email": fields.String(readOnly=True),
})

# http://127.0.0.1:5000/users/

@api.route("/")
class UserListCreate(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return [user.to_dict() for user in UserProvider.get_users_pr()], 200

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model)
    def post(self):
        data = api.payload
        user = UserProvider.create_user_pr(data)
        return user.to_dict(), 201

@api.route("/<int:user_id>")
class UserGetUpdateDelete(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        user = UserProvider.get_user_pr(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict()

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        data = api.payload
        updated_user = UserProvider.update_user_pr(user_id, data)
        return updated_user.to_dict(), 200

    def delete(self, user_id):
        UserProvider.delete_user_pr(user_id)
        print("deleted user")
        return None, 204

    def patch(self, user_id):
        pass
