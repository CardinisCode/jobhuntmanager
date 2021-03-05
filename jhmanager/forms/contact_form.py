from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField, DateField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from datetime import datetime
from flask_fontawesome import FontAwesome


# class ContactMeForm(FlaskForm):
