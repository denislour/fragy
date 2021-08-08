from flask import Flask
from pallets.core.configs import configs
from pallets.core.blueprints import blueprints
from pallets.core.extensions import extensions


def create_app(settings_override=None):
    """
        Create application by using factory pattern.
        :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # Config
    configs(app, settings_override)

    # Blueprints
    blueprints(app)

    # Extensions
    extensions(app)

    return app
