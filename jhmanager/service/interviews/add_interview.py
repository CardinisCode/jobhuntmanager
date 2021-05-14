from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "application_id": application_id,
        "company_name": company.name, 
        "action_url": '/applications/{}/add_interview'.format(application_id)
    }

    return render_template('add_interview.html', add_interview_form=add_interview_form, details=details)


def InsertFieldsIntoInterviewHistory(interview_fields, interviewsRepo): 
    # Lets make sure none of the fields have been left empty by the user:
    for heading, value in interview_fields.items():
        if value == "":
            interview_fields[heading] = "N/A"

    # Lets grab the date & time provided by the user:
    entry_date = interview_fields["entry_date"]
    interview_date = interview_fields["interview_date"]
    interview_time = interview_fields["interview_time"]

    # Now to convert the date & time values to string:
    date_format = "%Y-%m-%d"
    date_str = interview_date.strftime(date_format)
    interview_fields["interview_date"] = date_str

    time_format = "%H:%M"
    time_str = interview_time.strftime(time_format)
    interview_fields["interview_time"] = time_str

    entry_date_str = entry_date.strftime(date_format)
    interview_fields["entry_date"] = entry_date_str

    # Now let's insert our values into interview_history:
    interview_id = interviewsRepo.CreateInterview(interview_fields)

    # If it gets here, the new interview has been successfully added to the repo.
    return interview_id


def check_if_interview_is_past_dated(interview_date, interview_time):
    # Lets structure our Interview date & time
    interview_date = interview_date
    interview_time = interview_time

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


def update_interview_stage_in_applications_repo(interviewsRepo, application_id, applicationsRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    current_interview_stage = application.interview_stage
    all_interviews_for_app_id = interviewsRepo.getInterviewsByApplicationID(application_id)
    interview_count = 0

    if all_interviews_for_app_id:
        for interview in all_interviews_for_app_id:
            interview_count += 1

    fields = {
        "interview_stage": interview_count, 
        "application_id": application_id
    }

    message = applicationsRepo.updateInterviewStageByID(fields)
    flash(message)


def post_add_interview(session, user_id, form, interviewsRepo, applicationsRepo, application_id, companyRepo):
    #Grab and verify field data:

    # We'll need these values for the conditional logic we'll need in a bit:
    interview_date = form.interview_date.data
    interview_time = form.interview_time.data
    status = form.status.data
    
    # The fields we'll need for our SQL insert query:
    interview_fields = {
        "application_id": application_id,
        "user_id": user_id, 
        "entry_date": datetime.now().date(),
        "interview_date": form.interview_date.data, 
        "interview_time": form.interview_time.data, 
        "interview_type": form.interview_type.data, 
        "interview_location": form.interview_location.data, 
        "interview_medium": form.interview_medium.data, 
        "other_medium": form.other_medium.data,
        "contact_number": form.phone_call.data, 
        "status": form.status.data,
        "interviewer_names": form.interviewer_names.data,
        "video_link": form.video_link.data,
        "extra_notes": form.extra_notes.data
    }

    # I want to check if the interview  date & time are future dated or in the past. 
    # & if its a past-dated interview, we want the user to verify if they've had the interview or if it was cancelled.
    # This will be a boolean value where yes = the interview is past-dated.
    past_interview = check_if_interview_is_past_dated(interview_date, interview_time)
    if past_interview and status == "upcoming": 
        flash("The interview date & time provided are past-dated. If this is correct, please choose the appropriate status for this interview.")
        return display_add_interview(form, application_id, applicationsRepo, companyRepo)

    # Add details to interview_history in SQL DB:
    interview_id = InsertFieldsIntoInterviewHistory(interview_fields, interviewsRepo)

    # Now we can update interview stage for this user:
    update_interview_stage_in_applications_repo(interviewsRepo, application_id, applicationsRepo)

    redirect_url = "/applications/{}/interview/{}".format(application_id, interview_id)

    return redirect(redirect_url)

