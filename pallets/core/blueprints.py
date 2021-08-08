from pallets.blueprints.page import page


def blueprints(app):
    """
        Register the blueprint (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    app.register_blueprint(page)
