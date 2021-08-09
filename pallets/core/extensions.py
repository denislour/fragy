from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_wtf import CSRFProtect


debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CSRFProtect()


def extensions(app):
    """
        Register the extensions (mutates the app passing in).

        :params: Flask app instance
        :return: None
    """
    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
