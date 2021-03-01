from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional

class AddNotesForm(FlaskForm):
    description = StringField(
        "Description for the Note", 
        validators=[InputRequired(message="Please provide a heading/description for this note.")],
        render_kw={'placeholder': "A description/heading for this note."},
    )

    notes = TextAreaField(
        "Notes", 
        validators=[InputRequired(message="Your notes field is empty.")],
        render_kw={'placeholder': "Your notes go here."},
    )

    save_notes = SubmitField("Save Notes")
    cancel_and_return = SubmitField("Cancel & Return to Application")
    