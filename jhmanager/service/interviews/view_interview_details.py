from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_fields_for_single_interview
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_company_fields import prepare_company_website_url
from datetime import datetime, time


def display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    interview = interviewsRepo.grabInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    general_details = {
        "application_details": {},
        "company_details": {}, 
        "links": {}
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description), 
        "location": replace_na_value_with_none(company.location)
    }

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "job_description": replace_na_value_with_none(application.job_description), 
        "interview_stage": cleanup_interview_stage(application.interview_stage)
    }


    website_link = prepare_company_website_url(company)
    general_details["links"] = {
        "company_website": website_link,
        "company_profile": '/company/{}/view_company'.format(company.company_id), 
        "update_interview": "/applications/{}/interview/{}/update_interview".format(application_id, interview_id),
        "delete_interview": "/applications/{}/interview/{}/delete_interview".format(application_id, interview_id),
        "view_interview_prep_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id), 
        "view_application": '/applications/{}'.format(application_id), 
        "view_notes_url": '/applications/{}/view_application_notes'.format(application_id), 
    }

    other_medium = interview.other_medium
    interview_details = {
        "fields": {}
    }
    interview_details["fields"] = {
        "interview_id": interview_id,
        "date": interview.interview_date, 
        "time": interview.interview_time, 
        "interview_type": interview.interview_type, 
        "status":  interview.status,
        "medium": interview.medium, 
        "location": interview.location, 
        "interviewer_names": interview.interviewer_names, 
        "extra_notes": interview.extra_notes,
        "contact_number": interview.contact_number, 
        "past_dated": False,
        "video_link": interview.video_link,
        "display_video_link": False 
    }
    cleanup_fields_for_single_interview(interview_details, other_medium)

    return render_template("view_interview_details.html", general_details=general_details, interview_details=interview_details)
