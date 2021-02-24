from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time

from jhmanager.service.display_add_interview_form import display_add_interview


def InsertFieldsIntoInterviewHistory(user_id,interviewsRepo, application_id, interview_date, interview_time, interview_type, interview_location, video_medium, other_medium, contact_number, status, interviewers):
    interview_type = interview_type.data

    interviewers = interviewers.data
    if not interviewers:
        interviewers = "N/A"

    location = interview_location.data
    if not location:
        location = "N/A"

    medium = video_medium.data
    if not medium:
        medium = "N/A"

    other_medium = other_medium.data
    if not other_medium:
        other_medium = "N/A"

    contact_number = contact_number.data
    if not contact_number:
        contact_number = "N/A"

    status = status.data
    if not status: 
        status = "upcoming"

    # Lets grab the date & time provided by the user:
    interview_date = interview_date.data
    interview_time = interview_time.data

    # Now to convert the date & time values to string:
    date_format = "%Y-%m-%d"
    app_date_str = interview_date.strftime(date_format)
    time_format = "%H:%M"
    app_time_str = interview_time.strftime(time_format)

    # application_id, interview_date, interview_time, interview_type, interview_location, video_medium, other_medium, contact_number, status, interviewers

    # Now let's insert our values into interview_history:
    fields = (user_id, application_id, app_date_str, app_time_str, interview_type, location, medium, other_medium, contact_number, status, interviewers)
    interviewsRepo.InsertNewInterviewDetails(fields)

    # If it gets here, the new interview has been successfully added to the repo.
    return True


def check_if_interview_is_past_dated(interview_date, interview_time):
    # Lets structure our Interview date & time
    interview_date = interview_date.data
    interview_time = interview_time.data
    # interview_date_str = interview_date.strftime(date_format)
    # interview_time_str = interview_time.strftime(time_format)

    # As a comparison point, we need to grab today's date & time 
    # Plus we have to make sure these values are in the same format as the interview date & time:
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_datetime_str = current_datetime.strftime("%m/%d/%Y, %H:%M")
    date_time_obj = datetime.strptime(current_datetime_str, "%m/%d/%Y, %H:%M")
    current_time = date_time_obj.time()

    if interview_date < current_date: 
        return True

    if interview_date == current_date:
        if interview_time <= current_time:
            return True

    return False


def post_add_interview(session, user_id, form, interviewsRepo, applicationsRepo, application_id, companyRepo):
    #Grab and verify field data:
    # company_name = form.company_name 
    interview_date = form.interview_date
    interview_time = form.interview_time
    interview_type = form.interview_type
    interviewers = form.interviewer_names
    interview_location = form.interview_location
    video_medium = form.interview_medium
    other_medium = form.other_medium
    contact_number = form.phone_call
    status = form.status

    # I want to check if the interview  date & time are future dated or in the past. 
    # & if its a past-dated interview, we want the user to verify if they've had the interview or if it was cancelled.
    # This will be a boolean value where yes = the interview is past-dated.
    past_interview = check_if_interview_is_past_dated(interview_date, interview_time)
    if past_interview and status.data == "upcoming": 
        flash("The interview date & time provided are past-dated. If this is correct, please choose the appropriate status for this interview.")
        return display_add_interview(form, application_id, applicationsRepo, companyRepo)

    redirect_url = "/applications/{}".format(application_id)

    # Add details to application_history in SQL DB:
    InsertFieldsIntoInterviewHistory(user_id, interviewsRepo, application_id, interview_date, interview_time, interview_type, interview_location, video_medium, other_medium, contact_number, status, interviewers)

    return redirect(redirect_url)

