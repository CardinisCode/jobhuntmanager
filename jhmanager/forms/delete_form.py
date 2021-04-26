from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators
from wtforms.validators import InputRequired


class DeleteCompanyForm(FlaskForm):
    confirm_choice = SelectField(
        "Confirm your choice", 
        choices=[(1, "No"),(0, "Yes")], 
        coerce=int,
        validators=[InputRequired()],
    )
    
    delete_button = SubmitField("Submit")