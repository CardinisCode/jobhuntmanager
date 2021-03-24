from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField, DateField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from datetime import datetime
from flask_fontawesome import FontAwesome


class AddCompanyJobApplicationForm(FlaskForm):
    date_posted = DateField(
        "Date Posted: ",
        [validators.optional()], 
        render_kw={'placeholder': "YYYY-MM-DD. The date that this job advert was posted."},
    )

    job_role = StringField(
        "Job Role / Position: ", 
        validators=[InputRequired(message="Which job role have you applied for?")], 
        render_kw={'placeholder': "The job role you're applying for."},
    )

    emp_type = SelectField(
        "Employment Type: ", 
        choices=[
            ("full_time", "Full Time"), 
            ("part_time", "Part Time"), 
            ("temp", "Temporary"), 
            ("contract", "Contract"), 
            ("other_emp_type", "Other")
        ],
        default="full_time")

    job_ref = StringField(
        "Job Reference: ", 
        [validators.optional()], 
        render_kw={'placeholder': "A reference for this job if provided."},
    )

    job_description = TextAreaField(
        "Job Description: ", 
        [validators.optional()], 
        render_kw={'placeholder': "All info provided regarding the job role itself."},
        description="You can copy in all the text provided regarding the role itself here."
    )

    job_perks = TextAreaField(
        "Job perks: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Job perks / benefits mentioned in the job posting."},
        description="What are they offering you in the job post?",
    )

    tech_stack = TextAreaField(
        "Tech Stack: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The technologies you'll be working with in this role, if mentioned."},
        description="The technologies you'll be working with in this role.",
    )

    salary = StringField(
        "Salary/Rates: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Annual/monthly/hourly Salary/Wages. "},
        description="If the job post provides the annual salary / hourly rate, it can go here.",
    )

    platform = StringField(
        "Job platform / board: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The platform / site / job board where you found this job posting."},
        description="Job platform / board where you found this role, if applicable.",
    )

    job_url = URLField(
        "Job URL: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The website link for the platform / job board where you found this job posting."},
        description="Where (website) did you find this job post?",
        default="http://...", 
    )

    user_notes = TextAreaField(
        "Your notes: ", 
        [validators.optional()],
        render_kw={'placeholder': "Your own notes / data from the job spec."},
        description="You can add your own notes or just use this to copy in content from the job post.",
    )

    save_button = SubmitField("Save")
