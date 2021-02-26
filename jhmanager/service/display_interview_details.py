from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


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
    # other_medium = interview_details.other_medium

    details["fields"] = { 
        "Date": interview_details.interview_date,
        "Time": interview_details.interview_time,
        "Type": interview_details.interview_type,
        "Status": interview_details.status,
        "Medium": medium, 
        "Location": interview_details.location,
        "Interviewer Names": interview_details.interviewer_names
    }

    

    return render_template("view_interview_details.html", details=details)
