from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators
from wtforms.fields.html5 import DateField, EmailField
import wtforms.widgets.html5
from wtforms.validators import InputRequired, Optional, Length, EqualTo
from datetime import datetime
from flask_fontawesome import FontAwesome


class UpdateEmailAddressForm(FlaskForm):
    email = EmailField(
        "Email Address: ", 
        validators=[InputRequired(message="Please provide your email address")],
        render_kw={'placeholder': "The email address you'd like to use."}, 
    )

    confirm_email = EmailField(
        "Confirm Email Address: ", 
        validators=[
            InputRequired(message="Please confirm your email address"),
            EqualTo('email', message="Both email address fields should match.")
        ],
        render_kw={'placeholder': "Confirm the email address you'd like to use."},
    )
    
    update_button = SubmitField("Update details") 


class UpdateUserNameForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[InputRequired(message="This is a required field.")],
        render_kw={'placeholder': "The username you'd like to use."},         
    )

    update_username = SubmitField("Update details") 


class ChangePasswordForm(FlaskForm):
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

    save_password = SubmitField("Save Password")

