from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators
from wtforms.validators import InputRequired


class DeleteCompanyForm(FlaskForm):
    confirm_choice = SelectField(
        "Confirm your choice", 
        choices=[], 
        coerce=int,
        validators=[InputRequired()],
    )
    
    delete_button = SubmitField("Submit")



            #     ("yes", "Yes, please delete this company profile."), 
            # ("no", "No, take me back to the company profile.")