from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional


class UpdateCompany(FlaskForm):
    name = StringField(
        "Company Name", 
        [validators.optional()], 
        render_kw={'placeholder': "The name of the company you're applying to work for."},
    )

    description = TextAreaField(
        "Description of the company", 
        [validators.optional()], 
        render_kw={'placeholder': "A description of the company provided."},
    )

    location = StringField(
        "Company Location / Head Office", 
        [validators.optional()], 
        render_kw={'placeholder': "Where is the company located? If entirely remote, where is their Head Office/Main base of operations?"},
    )

    industry = StringField(
        "Industry", 
        [validators.optional()], 
        render_kw={'placeholder': "The industry/industries in which this company operates."},        
    )

    interviewers = StringField(
        "Interviewer/s' Name/s", 
        [validators.optional()], 
        render_kw={'placeholder': "The name/s of the interviewer/s for this interview. (If known)"},         
    )

    contact_number = TelField(
        "Telephone / Mobile number", 
        [validators.optional()], 
        render_kw={'placeholder': "The contact number for the interviewers / company."}, 
        description="The number you'll be expecting a call from for this interview."       
    )

    url = URLField(
        "The Company's Website (Link)", 
        [validators.optional()], 
        render_kw={'placeholder': "The url for the company's website."},          
    )

    update_company = SubmitField("Update")

