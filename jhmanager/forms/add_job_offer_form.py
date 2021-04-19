from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, validators
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField


class AddJobOffer(FlaskForm):
    job_role = StringField(
        "Job Role: ", 
        validators=[InputRequired(message="Job role on offer")], 
        render_kw={'placeholder': "Which job role is offer by the company?"},
    )

    salary_offered = StringField(
        "Salary: ", 
        [validators.optional()], 
        render_kw={'placeholder': "Salary on Offer."},
    )

    perks_offered = TextAreaField(
        "Perks Offered with the role: ", 
        [validators.optional()], 
        render_kw={'placeholder': "All job perks offered alongside the salary. EG: Stock options."},
    )

    offer_response = SelectField(
        "Offer: ", 
        choices=[
            ("user_accepted", "I Accepted!"), 
            ("user_declined", "I Declined"), 
            ("company_pulled_offer", "Company pulled offer"), 
            ("undecided", "I am still deciding")
        ]
    )

    starting_date = DateField(
        "Starting Date: ",
        [validators.optional()], 
        render_kw={'placeholder': "Date you start working at this company, if applicable. YYY-MM-DD"},
    )

    save_button = SubmitField("Save Job Offer")

