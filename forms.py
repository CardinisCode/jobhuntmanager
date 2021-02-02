from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from datetime import datetime


class AddApplicationForm(FlaskForm):
    job_role = StringField(
        "Job Role: ", 
        validators=[InputRequired(message="Which job role have you applied for?")], 
        render_kw={'placeholder': "The job role you're applying for."},
        default="N/A", 
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
        default="N/A", 
    )

    company_name = StringField(
        "Company Name: ", 
        validators=[InputRequired(message="Please provide the name of the Company/Recruitment firm you're interviewing with.")], 
        render_kw={'placeholder': "Name of the Company you'd be working for directly."},
        default="N/A", 
    )

    company_description = TextAreaField(
        "Company Description: ", 
        [validators.optional()], 
        description="All info relevant to the company.",
        render_kw={'placeholder': "Description of company provided in Job Spec or from research."},
        default="N/A", 
    )

    job_description = TextAreaField(
        "Job Description: ", 
        [validators.optional()], 
        default="N/A", 
        render_kw={'placeholder': "All info provided regarding the job role itself."},
        description="You can copy in all the text provided regarding the role itself here."
    )

    job_perks = TextAreaField(
        "Job perks: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Job perks / benefits mentioned in the job posting."},
        description="What are they offering you in the job post?",
        default="N/A", 
    )
    
    tech_stack = TextAreaField(
        "Tech Stack: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The technologies you'll be working with in this role, if mentioned."},
        description="The technologies you'll be working with in this role.",
        default="N/A", 
    )

    location = StringField(
        "Interview Location: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Where is the company located? (if you're working from an office/branch/store)"},
        description="Where are their offices and/or where will you be working?",
        default="Remote", 
    )

    salary = StringField(
        "Salary/Rates: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Annual/monthly/hourly Salary/Wages. "},
        description="If the job post provides the annual salary / hourly rate, it can go here.",
        default="N/A", 
    )

    user_notes = TextAreaField(
        "Your notes: ", 
        [validators.optional()],
        render_kw={'placeholder': "Your own notes / data from the job spec."},
        description="You can add your own notes or just use this to copy in content from the job post.",
        default="N/A", 
    )

    platform = StringField(
        "Job platform / board: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The platform / site / job board where you found this job posting."},
        description="Job platform / board where you found this role, if applicable.",
        default="N/A", 
    )

    job_url = URLField(
        "Job URL: ", 
        [validators.optional()], 
        render_kw={'placeholder': "The website link for the platform / job board where you found this job posting."},
        description="Where (website) did you find this job post?",
        default="http://...", 
    )

    save_application = SubmitField("Save")


class AddInterviewForm(FlaskForm):
    todays_date = datetime.now()
    current_time = datetime.now().time

    #Fields to display:
    company_name = StringField("Company Name: ", validators=[InputRequired(message="Please provide the name of the Company/Recruitment firm you're interviewing with.")])
    interview_date = DateField("Date: ", validators=[InputRequired(message="Please provide the Interview Date.")], format='%Y-%m-%d', default=todays_date)
    interview_time = TimeField("Time: ", validators=[InputRequired(message="Please provide the starting time for the interview.")], format='%H:%M', default=current_time)
    job_role = StringField("Job Role: ", [validators.optional()])
    interviewer_names = StringField("Interviewer Names: ", [validators.optional()], default="Unknown at present")
    interview_type = SelectField("Interview Type: ", choices=[
        ('in_person', 'In Person / On Site'),
        ('video_or_online', 'Video / Online'), 
        ('phone_call', 'Telephone Call')
    ])
    interview_location = StringField("Interview Location: ", [validators.optional()], default="Remote")
    interview_medium = SelectField("Video Interview Medium: ", choices=[
        ('skype', 'Skype'),
        ('zoom', 'Zoom'),
        ('google_chat', 'Google Chat'),
        ('meet_jit_si', 'Meet.jit.si'),
        ('other', 'Other')
    ])
    other_medium = StringField("Other Medium: ", [validators.optional()], default="N/A")
    phone_call = TelField("Telephone Call: ", [validators.optional()], default="N/A")
    status = SelectField("Interview Status: ", choices=[
        ('upcoming', 'Upcoming Interview'), 
        ('done', 'Interview Done'), 
        ('cancelled', 'Interview Cancelled'), 
        ('post-poned', 'Interview has been post-poned')
    ], default='upcoming')

    save_button = SubmitField("Save")



