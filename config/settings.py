DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'secret_key'
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Flask-Mail.
# MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'email@gmail.com'
MAIL_PASSWORD = 'secret_password'
