from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def add_company_details(details, company):
    details["company_details"] = {
        "Name" : company.name, 
        "Description" : company.description, 
        "Location" : company.location, 
        "Industry" : company.industry, 
        "Website" : company.url,
    }

def cleanup_fields(details, other_medium):
    # I want to clean up a few fields to improve how they're displayed:
    interview_type = details["interview_fields"]["Type"]
    # interview_date = details["fields"]["Date"]
    # interview_time = details["fields"]["Time"]
    interview_medium = details["interview_fields"]["Medium"]
    interviewer_names = details["interview_fields"]["Interviewer Names"]
    # status = details["fields"]["Status"]

    if interviewer_names == "Unknown at present":
        details["interview_fields"]["Interviewer Names"] = ""

    if interview_medium == "google_chat":
        details["interview_fields"]["Medium"] = "Google Chat"

    elif interview_medium == "meet_jit_si":
        details["interview_fields"]["Medium"] = "Meet.Jit.Si"

    elif interview_medium == "other":
        details["interview_fields"]["Medium"] = other_medium

    else:
        details["interview_fields"]["Medium"] = interview_medium.capitalize()

    
    if interview_type == "in_person":
        details["interview_fields"]["Type"] = "In Person / On Site"

    elif interview_type == "video_or_online":
        details["interview_fields"]["Type"] = "Video / Online"

    else:
        details["interview_fields"]["Type"] = "Phone Call"


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
    }

    interview = interviewsRepo.grabInterviewByID(interview_id)
    interview_id = interview.interview_id
    application_id = interview.application_id
    medium = interview.medium
    other_medium = interview.other_medium

    details["interview_fields"] = { 
        "Date": interview.interview_date,
        "Time": interview.interview_time,
        "Type": interview.interview_type,
        "Status": interview.status.capitalize(),
        "Medium": medium, 
        "Location": interview.location,
        "Interviewer Names": interview.interviewer_names
    }

    cleanup_fields(details, other_medium)
    add_company_details(details, company)


    return render_template("view_interview_details.html", details=details)
