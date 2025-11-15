from flask_restx import Api
from resources.user_resource import api as user_ns


def register_routes(app):
    api = Api(app, version="1.0", title="Flask Restx User CRUD API")
    api.add_namespace(user_ns, path="/users")