from flask import Flask
from pallets.blueprints.page import page
from pallets.blueprints.contact import contact


def blueprints(app: Flask):
    """
        Register the blueprint (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    app.register_blueprint(page)
    app.register_blueprint(contact)
