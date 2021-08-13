from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import Length, DataRequired


class ContactForm(FlaskForm):
    email = EmailField(
        "What's your e-mail address", [DataRequired(), Length(3, 254)])
    message = TextAreaField(
        "What's is you question issue", [DataRequired(), Length(1, 7999)])
