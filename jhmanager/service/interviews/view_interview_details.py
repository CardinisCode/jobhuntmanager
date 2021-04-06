from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from datetime import datetime, time


def add_company_details(details, company):
    details["company_details"] = {
        "company_name" : company.name, 
        "view_company_url": '/company/{}/view_company'.format(company.company_id)
    }

def cleanup_fields(details, other_medium):

    # I want to clean up a few fields to improve how they're displayed:
    interview_type = details["interview_fields"]["interview_type"]
    interview_medium = details["interview_fields"]["medium"]
    interviewer_names = details["interview_fields"]["interviewer_names"]
    video_link = details["interview_fields"]["video_link"]
    location = details["interview_fields"]["location"]
    interview_time = details["interview_fields"]["time"]

    if interviewer_names == "Unknown at present":
        details["interview_fields"]["Interviewer Names"] = None

    if interview_medium == "google_chat":
        details["interview_fields"]["medium"] = "Google Chat"

    elif interview_medium == "meet_jit_si":
        details["interview_fields"]["medium"] = "Meet.Jit.Si"

    elif interview_medium == "other":
        details["interview_fields"]["medium"] = other_medium

    else:
        details["interview_fields"]["medium"] = interview_medium.capitalize()

    if interview_type == "in_person":
        details["interview_fields"]["interview_type"] = "In Person / On Site"

    elif interview_type == "video_or_online":
        details["interview_fields"]["interview_type"] = "Video / Online"

    else:
        details["interview_fields"]["interview_type"] = "Phone Call"

    if video_link == "N/A":
        details["interview_fields"]["video_link"] = None

    if location == "N/A":
        details["interview_fields"]["location"] = None

    

    interview_time_str = interview_time.strftime("%H")
    # interview_time_obj = datetime.strptime(interview_time, '%H:%M')
    hour_int = int(interview_time.strftime("%H"))
    if hour_int >= 12:
        interview_time_str += "pm"
    else:
        interview_time_str += "am"
    details["interview_fields"]["time"] = interview_time_str

    return True


def display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo):
    application_details = applicationsRepo.grabApplicationDetailsByApplicationID(application_id)

    for application in application_details:
        company_id = application[2]

    company = companyRepo.getCompanyById(company_id)
    company_name = company.name

    details = {
        "app_id": application_id, 
        "interview_id": interview_id, 
        "company_name": company_name,
        "update_url": "/applications/{}/interview/{}/update_interview".format(application_id, interview_id),
        "delete_url": "/applications/{}/interview/{}/delete_interview".format(application_id, interview_id),
        "view_interview_prep_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id), 
        "return_to_application": '/applications/{}'.format(application_id), 
        "view_notes_url": '/applications/{}/view_application_notes'.format(application_id)
    }

    interview = interviewsRepo.grabInterviewByID(interview_id)
    interview_id = interview.interview_id
    application_id = interview.application_id
    medium = interview.medium
    other_medium = interview.other_medium

    details["interview_fields"] = { 
        "date": interview.interview_date,
        "time": interview.interview_time,
        "interview_type": interview.interview_type,
        "status": interview.status.capitalize(),
        "medium": medium, 
        "location": interview.location,
        "interviewer_names": interview.interviewer_names, 
        "video_link": interview.video_link, 
        "contact_number": interview.contact_number
    }

    cleanup_fields(details, other_medium)
    add_company_details(details, company)


    return render_template("view_interview_details.html", details=details)
