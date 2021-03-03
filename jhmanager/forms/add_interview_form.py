from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, validators
from wtforms.fields.html5 import TelField, URLField, DateField, TimeField
import wtforms.widgets.html5
from wtforms.validators import DataRequired, Email, InputRequired, Optional, ValidationError
from datetime import datetime, date, time

from wtforms_components import DateRange


class AddInterviewForm(FlaskForm):
    todays_datetime = datetime.now()
    todays_date = datetime.now().date().strftime("%Y-%m-%d")
    current_time = datetime.now().time().strftime("%H:%M")

    #Fields to display:
    interview_date = DateField(
        "Interview Date: ", 
        format='%Y-%m-%d',
        validators=[
            InputRequired(message="Please provide the Interview Date.")
        ], 
    )

    interview_time = TimeField(
        "Interview Time: ", 
        validators=[
            InputRequired(message="Please provide the starting time for the interview.")
        ], 
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
