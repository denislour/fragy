from flask_wtf import Form
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import Length, DataRequired


class ContactForm(Form):
    email = EmailField(
        "What's your e-mail address", [DataRequired(), Length(3, 254)])
    message = TextAreaField(
        "What's is you question issue", [DataRequired(), Length(1, 7999)])
