from flask import Flask
from config import Config
from routes.user_routes import register_routes
from extensions.db import db


def create_app():
    print("in create app")
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)