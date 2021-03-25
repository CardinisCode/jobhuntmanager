from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class AddCompanyNoteForm(FlaskForm):
    subject = StringField(
        "Subject for the Note: ", 
        validators=[InputRequired(message="Please provide a heading/subject for this note.")],
        render_kw={'placeholder': "A description/heading for this note."},
    )

    note_text = TextAreaField(
        "Notes: ", 
        validators=[InputRequired(message="Your notes field is empty.")],
        render_kw={'placeholder': "Your notes go here."},
    )

    save_button = SubmitField("Save Note")
