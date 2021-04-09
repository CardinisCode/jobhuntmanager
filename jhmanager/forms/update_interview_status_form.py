from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, validators
import wtforms.widgets.html5
from wtforms.validators import InputRequired, ValidationError


class UpdateInterviewStatusForm(FlaskForm):
    status = SelectField(
        "Interview Status: ", 
        choices=[
            ('upcoming', 'Upcoming Interview'), 
            ('done', 'Interview Done'), 
            ('cancelled', 'Interview Cancelled'), 
            ('post-poned', 'Interview has been post-poned')
        ], 
    ) 
  
    save_button = SubmitField("Save Changes")