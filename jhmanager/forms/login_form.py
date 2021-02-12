from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators, PasswordField
from wtforms.validators import Length, EqualTo, email_validator, Email, InputRequired, ValidationError, Optional, DataRequired
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5


class LoginForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[InputRequired(message="Username required.")], 
        render_kw={'placeholder': "Your username."},
    )

    password = PasswordField(
        "Password: ", 
        validators=[InputRequired(message="Password required.")],
        render_kw={'placeholder': "Your password."},
    )

    login_button = SubmitField("Login")