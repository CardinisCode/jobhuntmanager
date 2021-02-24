from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional, ValidationError
from datetime import datetime, date, time


class AddInterviewPrepForm(FlaskForm):
    interview_question = StringField(
        "Question: ",
        validators=[InputRequired(message="Which Question would you like to prepare for?")],
        render_kw={'placeholder': "The Question you'd like to prepare for."},
    ), 

    answer_text = StringField(
        "Answer:", 
        validators=[InputRequired(message="How would you like to answer this question?")],
        render_kw={'placeholder': "Your answer to the above Question."},
    ), 
    save_preparation = SubmitField("Save your preparation")