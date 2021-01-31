from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def InsertFieldsIntoInterviewHistory(interviewsRepo, user_id, company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number):
    company_name = company_name.data
    interview_date = str(interview_date.data)
    interview_time = str(interview_time.data)
    interview_type = interview_type.data

    job_role = job_role.data
    if not job_role: 
        job_role = "N/A"

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

    insert_values = interviewsRepo.InsertNewInterviewDetails(user_id, company_name, interview_date, interview_time, job_role, interviewers, interview_type, location, medium, other_medium, contact_number)

    # For Development purposes, if this function ever fails to insert the values, we need an error message flashing to notify us:
    if not insert_values:
        flash("Failed to insert values into InterviewHistoryRepo. Please investigate!")
        return False

    # If it gets here, the new interview has been successfully added to the repo.
    return True



def gather_details_and_add_to_display_dict(company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number):
    details = {}

    # Gather all fields to be displayed to user as confirmation:
    details["company_name"] = {
        "label": "Company Name", 
        "data": company_name
    }

    details["interview_date"] = {
        "label": "Date", 
        "data": interview_date
    }

    details["interview_time"] = {
        "label": "Time", 
        "data": interview_time
    }

    details["job_role"] = {
        "label": "Job Role", 
        "data": job_role
    }

    details["interview_type"] = {
        "label": "Type", 
        "data": interview_type
    }

    # Setting conditions for which data gets presents to the screen, 
    # depending on which options the user selects:
    if interviewers.data != "Unknown at present":
        details["interviewers"] = {
            "label": "Interviewers' names", 
            "data": interviewers
        }

    if interview_type.data == 'in_person':
        details["interview_location"] = {
            "label": "Location", 
            "data": interview_location
        }

    if interview_type.data == 'video_or_online':
        details["video_medium"] = {
            "label": "Video / Online", 
            "data": video_medium
        } 

    if interview_type.data == 'video' and video_medium == 'other':
        details["other_medium"] = {
            "label": "Other Medium", 
            "data": other_medium
        } 

    if interview_type.data == 'phone_call': 
        details["phone_call"] = {
            "label": "Contact Number",
            "data": contact_number
        } 

    return details



def post_add_interview(session, user_id, form, interviewsRepo):
    #Grab and verify field data:
    company_name = form.company_name 
    interview_date = form.interview_date
    interview_time = form.interview_time
    interview_type = form.interview_type
    job_role = form.job_role
    interviewers = form.interviewer_names
    interview_location = form.interview_location
    video_medium = form.interview_medium
    other_medium = form.other_medium
    contact_number = form.phone_call

    # Add details to SQL DB:
    InsertFieldsIntoInterviewHistory(interviewsRepo, user_id, company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number)

    # Add details to a dict to be displayed to the template
    details = gather_details_and_add_to_display_dict(company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number)

    return render_template("interview_details.html", details=details)


# def add_interview_details_to_interviewHistoryRepo()


