from flask import Flask


def create_app():
    """
        Create application by using factory pattern.
        :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        return "Hello Word"

    return app
