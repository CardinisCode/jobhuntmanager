from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators, PasswordField
from wtforms.validators import Length, EqualTo, email_validator, Email, InputRequired, ValidationError, Optional, DataRequired
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5


class RegisterUserForm(FlaskForm):
    username = StringField(
        "Username: ", 
        validators=[
            Length(min=6, max=25), 
            InputRequired(message="Please provide an unique username.")
        ],
        render_kw={'placeholder': "An unique username, with a minimal of 6 characters & 1 digit."},
        description='<i class="fas fa-user"></i>'
    )

    email_address = StringField(
        "Email Address", 
        validators=[
            Length(min=6, max=35), 
            InputRequired(message="Please provide a username.")
        ],
        render_kw={'placeholder': "Your email address"},
    )

    password = PasswordField(
        "Password: ", 
        validators=[
            Length(min=6), 
            InputRequired(message="Please provide a password.")
        ],
        render_kw={'placeholder': "An unique password, with a minimal of 6 characters, 1 special character & 1 digit."},
    )

    confirm_password = PasswordField(
        "Confirm Password", 
        validators=[
            Length(min=6),
            InputRequired(message="Please provide a password."), 
            EqualTo('password', message="The passwords should match.")
        ],
        render_kw={'placeholder': "Please repeat your password here."},
    )

    register_button = SubmitField("Register")



