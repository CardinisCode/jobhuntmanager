from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, TimeField, SelectField, validators 
from wtforms.validators import DataRequired, Email, InputRequired, Optional


class AddInterviewForm(FlaskForm):
    # company_name = StringField("Company Name")
    company_name = StringField("Company Name: ", validators=[InputRequired(message="Please provide the name of the Company/Recruitment firm you're interviewing with.")])
    interview_date = DateField("Date: ", validators=[InputRequired(message="Please provide the Interview Date.")], format='%Y-%m-%d')
    interview_time = TimeField("Time: ", validators=[InputRequired(message="Please provide the starting time for the interview.")])
    job_role = StringField("Job Role: ")
    interviewer_names = StringField("Interviewer Names: ", default="Unknown at present")
    interview_type = SelectField("Interview Type: ", choices=[
        ('in_person', 'In Person / On Site'),
        ('video_or_online', 'Video / Online'), 
        ('phone_call', 'Telephone Call')
    ])
    interview_location = StringField("Interview Location: ", default="Remote")
    interview_medium = SelectField("Video Interview Medium: ", choices=[
        ('skype', 'Skype'),
        ('zoom', 'Zoom'),
        ('google_chat', 'Google Chat'),
        ('meet_jit_si', 'Meet.jit.si'),
        ('other', 'Other')
    ])
    other_medium = StringField("Other Medium: ", default="N/A")
    save_button = SubmitField("Save")