from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db

    db.init_app(app)

    from .plan import bp as plans

    app.register_blueprint(plans, url_prefix="/plans")

    from .users import bp as users

    app.register_blueprint(users, url_prefix="/users")

    @app.route("/")
    def hello():
        return "Hello, world!"

    return app
