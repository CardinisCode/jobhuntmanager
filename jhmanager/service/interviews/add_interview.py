from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from jhmanager.service.cleanup_files.cleanup_general_fields import get_count


def display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "application_id": application_id,
        "company_name": company.name, 
        "action_url": '/applications/{}/add_interview'.format(application_id)
    }

    return render_template('add_interview.html', add_interview_form=add_interview_form, details=details)


def InsertFieldsIntoInterviewHistory(add_interview_form, user_id, application_id, interviewsRepo): 
    # The fields we'll need for our SQL insert query:
    interview_fields = {
        "application_id": application_id,
        "user_id": user_id, 
        "entry_date": datetime.now().date(),
        "interview_date": add_interview_form.interview_date.data, 
        "interview_time": add_interview_form.interview_time.data, 
        "interview_type": add_interview_form.interview_type.data, 
        "interview_location": add_interview_form.interview_location.data, 
        "interview_medium": add_interview_form.interview_medium.data, 
        "other_medium": add_interview_form.other_medium.data,
        "contact_number": add_interview_form.phone_call.data, 
        "status": add_interview_form.status.data,
        "interviewer_names": add_interview_form.interviewer_names.data,
        "video_link": add_interview_form.video_link.data,
        "extra_notes": add_interview_form.extra_notes.data
    }

    # Lets make sure none of the fields have been left empty by the user:
    for heading, value in interview_fields.items():
        if value == "":
            interview_fields[heading] = "N/A"

    # Now to convert the date & time values (in our above dictionary) to string:
    date_format = "%Y-%m-%d"
    date_str = interview_fields["interview_date"].strftime(date_format)
    interview_fields["interview_date"] = date_str

    time_format = "%H:%M"
    time_str = interview_fields["interview_time"].strftime(time_format)
    interview_fields["interview_time"] = time_str

    entry_date_str = interview_fields["entry_date"].strftime(date_format)
    interview_fields["entry_date"] = entry_date_str

    # Now let's insert our values into interview_history:
    interview_id = interviewsRepo.CreateInterview(interview_fields)

    # If it gets here, the new interview has been successfully added to the repo.
    return interview_id


def update_interview_stage_in_applications_repo(interviewsRepo, application_id, applicationsRepo):
    all_interviews_for_app_id = interviewsRepo.getInterviewsByApplicationID(application_id)
    interview_count = get_count(all_interviews_for_app_id)

    fields = {
        "interview_stage": interview_count, 
        "application_id": application_id
    }

    return applicationsRepo.updateInterviewStageByID(fields)


def post_add_interview(user_id, add_interview_form, interviewsRepo, applicationsRepo, application_id, companyRepo):
    #Grab and verify field data:

    # We'll need these values for the conditional logic we'll need in a bit:
    interview_date = add_interview_form.interview_date.data
    interview_time = add_interview_form.interview_time.data
    status = add_interview_form.status.data

    # I want to check if the interview  date & time are future dated or in the past. 
    # & if its a past-dated interview, we want the user to verify if they've had the interview or if it was cancelled.
    # This will be a boolean value where yes = the interview is past-dated.
    past_interview = past_dated(interview_date, interview_time)
    if past_interview and status == "upcoming": 
        flash("The interview date & time provided are past-dated. If this is correct, please choose the appropriate status for this interview.")
        return display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo)

    # Add details to interview_history in SQL DB:
    interview_id = InsertFieldsIntoInterviewHistory(add_interview_form, user_id, application_id, interviewsRepo)

    # Now we can update interview stage for this user:
    message = update_interview_stage_in_applications_repo(interviewsRepo, application_id, applicationsRepo)
    flash(message)
    redirect_url = "/applications/{}/interview/{}".format(application_id, interview_id)

    return redirect(redirect_url)

