from flask_wtf import FlaskForm
from wtforms import SubmitField, validators


class WarningForm(FlaskForm): 
    save_button = SubmitField("Save")