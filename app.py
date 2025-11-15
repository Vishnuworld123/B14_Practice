from flask import Flask
from config import Config
from routes.user_routes import register_routes
from extensions.db import db


def create_app():
    print("in create app-----------------")
    app = Flask(__name__)
    print("after defining app")
    app.config.from_object(Config)
    db.init_app(app)
    print("before table creation#############")
    
    with app.app_context():
        db.create_all()

    print("creted table")
    register_routes(app)
    print("before defining app")
    return app


if __name__ == "__main__":
    print("in if condition")
    app = create_app()
    app.run(debug=True)
