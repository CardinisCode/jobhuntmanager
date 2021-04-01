from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField, EmailField
from wtforms.validators import Email, InputRequired, Optional, ValidationError


class AddNewContactForm(FlaskForm):
    full_name = TextAreaField(
        "Full Name:", 
        validators=[
            InputRequired(message="Please provide the contact's First name & Surname.")
        ],  
        render_kw={'placeholder': "The contact's first and last name."},
    )

    job_title = TextAreaField(
        "Job Title:", 
        [validators.optional()], 
        render_kw={'placeholder': "The contact's job title."},
    )

    contact_number = TelField(
        "Telephone Call: ", 
        [validators.optional()],
        render_kw={'placeholder': "The telephone number for this contact."},
    )

    company_name = StringField(
        "Company Name:", 
        [validators.optional()], 
        render_kw={'placeholder': "The company where this contact works."},
    )

    email_address = EmailField(
        "Email Address: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The contact's email address."},
    )

    linkedin_profile = URLField(
        "Linkedin Profile: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The link to the contact's LinkedIn Profile."},
    )

    save_button = SubmitField("Save")






