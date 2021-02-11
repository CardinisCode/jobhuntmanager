from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional, ValidationError
from datetime import datetime, date, time

from wtforms_components import DateRange


class AddInterviewForm(FlaskForm):
    todays_datetime = datetime.now()
    todays_date = datetime.now().date()
    current_time = datetime.now().time()

    #Fields to display:
    company_name = StringField(
        "Company Name: ", 
        validators=[InputRequired(message="Please provide the name of the Company/Recruitment firm you're interviewing with.")],
        render_kw={'placeholder': "The name of the Company/Recruitment firm you're interviewing with."},
    )

    interview_date = DateField(
        "Date: ", 
        validators=[
            DateRange(min=date.today(), message="Please choose a date either present or in the future."), 
            InputRequired(message="Please provide the Interview Date.")
        ], 
        format='%Y-%m-%d', 
        default=todays_date, 
        render_kw={'placeholder': "The interview date. YYYY-MM-DD"},
    )

    interview_time = TimeField(
        "Time: ", 
        validators=[
            DateRange(min=current_time, message="Please choose a time either present or in the future."), 
            InputRequired(message="Please provide the starting time for the interview.")
        ], 
        format='%H:%M', 
        default=current_time, 
        render_kw={'placeholder': "The interview time. HH:MM"},
    )
    
    job_role = StringField(
        "Job Role: ", 
        [validators.optional()],
        render_kw={'placeholder': "The job role / position you're applied for."},
    )
    interviewer_names = StringField(
        "Interviewer Names: ", 
        [validators.optional()], 
        default="Unknown at present",
        render_kw={'placeholder': "The names of the interviewers, if known at this point."},
    )
    interview_type = SelectField(
        "Interview Type: ", 
        choices=[
            ('in_person', 'In Person / On Site'),
            ('video_or_online', 'Video / Online'), 
            ('phone_call', 'Telephone Call')
        ],
        default='video_or_online',
    )
    interview_location = StringField(
        "Interview Location: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Where will the interview be located. 'Remote' will be the default value."},
    )
    interview_medium = SelectField(
        "Video Interview Medium: ", 
        choices=[
            ('skype', 'Skype'),
            ('zoom', 'Zoom'),
            ('google_chat', 'Google Chat'),
            ('meet_jit_si', 'Meet.jit.si'),
            ('other', 'Other')
        ], 
    default='zoom', 

    )
    other_medium = StringField(
        "Other Medium: ", 
        [validators.optional()],
        render_kw={'placeholder': "Any other form of video medium, not mention in the above list."},
    )
    phone_call = TelField(
        "Telephone Call: ", 
        [validators.optional()],
        render_kw={'placeholder': "The telephone number you're expecting a call from, for this interview. If left blank, it will default to 'Unknown at present'."},
    )
    status = SelectField(
        "Interview Status: ", 
        choices=[
            ('upcoming', 'Upcoming Interview'), 
            ('done', 'Interview Done'), 
            ('cancelled', 'Interview Cancelled'), 
            ('post-poned', 'Interview has been post-poned')
        ], 
    default='upcoming',
    )
    save_button = SubmitField("Save")
