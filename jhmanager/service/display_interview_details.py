from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def cleanup_fields(details, other_medium):
    # I want to clean up a few fields to improve how they're displayed:
    interview_type = details["fields"]["Type"]
    # interview_date = details["fields"]["Date"]
    # interview_time = details["fields"]["Time"]
    interview_medium = details["fields"]["Medium"]
    interviewer_names = details["fields"]["Interviewer Names"]
    # status = details["fields"]["Status"]

    if interviewer_names == "Unknown at present":
        details["fields"]["Interviewer Names"] = ""

    if interview_medium == "google_chat":
        details["fields"]["Medium"] = "Google Chat"

    elif interview_medium == "meet_jit_si":
        details["fields"]["Medium"] = "Meet.Jit.Si"

    elif interview_medium == "other":
        details["fields"]["Medium"] = other_medium

    else:
        details["fields"]["Medium"] = interview_medium.capitalize()

    
    if interview_type == "in_person":
        details["fields"]["Type"] = "In Person / On Site"

    elif interview_type == "video_or_online":
        details["fields"]["Type"] = "Video / Online"

    else:
        details["fields"]["Type"] = "Phone Call"


    return True


def display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo):
    application_details = applicationsRepo.grabApplicationDetailsByApplicationID(application_id)

    for application in application_details:
        company_id = application[2]

    company_name = companyRepo.getCompanyById(company_id).name

    details = {
        "app_id": application_id, 
        "interview_id": interview_id, 
        "company_name": company_name,
    }

    interview_details = interviewsRepo.grabInterviewByID(interview_id)
    interview_id = interview_details.interview_id
    application_id = interview_details.application_id
    medium = interview_details.medium
    other_medium = interview_details.other_medium

    details["fields"] = { 
        "Date": interview_details.interview_date,
        "Time": interview_details.interview_time,
        "Type": interview_details.interview_type,
        "Status": interview_details.status.capitalize(),
        "Medium": medium, 
        "Location": interview_details.location,
        "Interviewer Names": interview_details.interviewer_names
    }

    cleanup_fields(details, other_medium)

    return render_template("view_interview_details.html", details=details)
