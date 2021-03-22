from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo):
    company_id = applicationsRepo.grabApplicationByID(application_id).company_id
    company_name = companyRepo.getCompanyById(company_id).name

    details = {
        "application_id": application_id, 
        "interview_id": interview_id, 
        "company_name": company_name, 
        "action_url": '/applications/{}/interview/{}/update_interview'.format(application_id, interview_id)
    }

    return render_template("update_interview.html", update_interview_form=update_interview_form, details=details)


def post_update_interview(update_interview_form, user_id, application_id, interview_id, interviewsRepo):
    # The interview date & time need to be in str format before added to the db:
    interview_date = update_interview_form.interview_date.data
    interview_time = update_interview_form.interview_time.data

    date_format = "%Y-%m-%d"
    time_format = "%H:%M"

    interview_date_str = interview_date.strftime(date_format)
    interview_time_str = interview_time.strftime(time_format)

    interview_details = {
        "interview_date" : interview_date_str, 
        "interview_time" : interview_time_str,
        "interviewer_names" : update_interview_form.interviewer_names.data,
        "interview_type" : update_interview_form.interview_type.data, 
        "interview_location" : update_interview_form.interview_location.data, 
        "interview_medium" : update_interview_form.interview_medium.data, 
        "other_medium" : update_interview_form.other_medium.data, 
        "phone_call" : update_interview_form.phone_call.data, 
        "status" : update_interview_form.status.data,
        "video_link": update_interview_form.video_link.data,
        "interview_id": interview_id,
        "application_id": application_id,
    }    
    # Now to use these details to use this interview in the DB:
    interviewsRepo.updateInterview(interview_details)

    flash("Interview details updated!")
    redirect_url = "/applications/{}/interview/{}".format(application_id, interview_id)
    return redirect(redirect_url)
