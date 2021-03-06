from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
import wtforms.widgets.html5
from wtforms.validators import InputRequired, Optional, ValidationError


class AddInterviewPrepForm(FlaskForm):
    question = StringField(
        "Question: ",
        validators=[InputRequired(message="Which Question would you like to prepare for?")],
        render_kw={'placeholder': "The Question you'd like to prepare for."},
    )

    answer = StringField(
        "Answer:", 
        validators=[InputRequired(message="How would you like to answer this question?")],
        render_kw={'placeholder': "Your answer to the above Question."},
    )
    save_button = SubmitField("Save your preparation")