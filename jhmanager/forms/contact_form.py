from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.fields.html5 import EmailField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from datetime import datetime
from flask_fontawesome import FontAwesome


class ContactMeForm(FlaskForm):
    full_name = StringField(
        "Name", 
        validators=[InputRequired(message="Please provide your name.")], 
        render_kw={'placeholder': "Your name."},
    )

    email = EmailField(
        "Email Address", 
        validators=[
            InputRequired(message="Please provide your name."), 
        ], 
        render_kw={'placeholder': "Your email address."},        
    )

    subject = StringField(
        "Subject", 
        validators=[InputRequired(message="Required field.")], 
        render_kw={'placeholder': "A subject for this message."},   
    )

    message = StringField(
        "Message", 
        validators=[InputRequired(message="Required field.")],
        render_kw={'placeholder': "Your message goes here."},
    )

    submit = SubmitField("Send")
