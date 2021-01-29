from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators 
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from datetime import datetime



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
    phone_call = StringField("Telephone Call: ", [validators.optional()], default="N/A")
    save_button = SubmitField("Save")


