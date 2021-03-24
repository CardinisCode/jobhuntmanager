from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class AddApplicationNoteForm(FlaskForm):
    description = StringField(
        "Subject for the Note: ", 
        validators=[InputRequired(message="Please provide a heading/description for this note.")],
        render_kw={'placeholder': "A description/heading for this note."},
    )

    notes_text = TextAreaField(
        "Notes: ", 
        validators=[InputRequired(message="Your notes field is empty.")],
        render_kw={'placeholder': "Your notes go here."},
    )

    save_button = SubmitField("Save Notes")
