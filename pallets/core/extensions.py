from flask_debugtoolbar import DebugToolbarExtension


debug_toolbar = DebugToolbarExtension()


def extensions(app):
    """
        Register the extensions (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    debug_toolbar.init_app(app)
