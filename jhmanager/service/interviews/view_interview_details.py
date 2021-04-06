from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_medium
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_fields_for_single_interview
from datetime import datetime, time


def add_company_details(details, company):
    details["company_details"] = {
        "company_name" : company.name, 
        "view_company_url": '/company/{}/view_company'.format(company.company_id)
    }


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

    interview_details = {}
    interview_details["fields"] = {
        "interview_id": interview_id,
        "date": interview.interview_date,
        "time": interview.interview_time,
        "interview_type": interview.interview_type,
        "status": interview.status.capitalize(),
        "medium": medium, 
        "location": interview.location,
        "interviewer_names": interview.interviewer_names, 
        "video_link": interview.video_link, 
        "contact_number": interview.contact_number, 
        "past_dated": False, 
        "display_video_link": False,
    }

    cleanup_fields_for_single_interview(interview_details, other_medium)
    add_company_details(details, company)

    return render_template("view_interview_details.html", details=details, interview_details=interview_details)
