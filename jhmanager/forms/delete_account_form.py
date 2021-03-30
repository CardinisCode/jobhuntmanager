from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired, Length


class DeleteAccountForm(FlaskForm):
    password = PasswordField(
        "Password: ", 
        validators=[
            Length(min=6), 
            InputRequired(message="Required field.")
        ],
        render_kw={'placeholder': "Your account password is required to delete this account."},
        description="Please provide your account password."
    )

    delete_button = SubmitField("Delete Account")


