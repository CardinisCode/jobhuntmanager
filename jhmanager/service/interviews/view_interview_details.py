from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_specific_interview
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_company_website
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from datetime import datetime, time


def display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    interview = interviewsRepo.getInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    other_medium = interview.other_medium
    interview_details = {}
    interview_details["fields"] = {
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
    cleanup_specific_interview(interview_details, other_medium)

    company_details = {}
    company_details["fields"] = {
        "name": company.name, 
        "description": company.description, 
        "location": company.location, 
        "industry": company.industry,
    }
    cleanup_specific_company(company_details)

    application_details = {}
    application_details["fields"] = {
        "job_role": application.job_role, 
        "job_description": application.job_description, 
        "interview_stage": application.interview_stage, 
        "emp_type": application.employment_type
    }
    cleanup_specific_job_application(application_details)

    general_details = {
        "application_details": application_details,
        "company_details": company_details, 
        "links": {}
    }

    general_details["links"] = {
        "company_website": cleanup_company_website(company.url),
        "company_profile": '/company/{}/view_company'.format(company.company_id), 
        "update_interview": "/applications/{}/interview/{}/update_interview".format(application_id, interview_id),
        "delete_interview": "/applications/{}/interview/{}/delete_interview".format(application_id, interview_id),
        "view_interview_prep_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id),
        "view_all_interview_prep": '/applications/{}/interview/{}/view_all_preparation'.format(application_id, interview_id), 
        "view_application": '/applications/{}'.format(application_id), 
        "view_application_notes": '/applications/{}/view_application_notes'.format(application_id), 
        "view_company_notes": '/company/{}/view_all_company_notes'.format(company.company_id), 
        "update_interview_status": '/applications/{}/interview/{}/update_interview_status'.format(application_id, interview_id), 
        "add_new_note": '/applications/{}/app_notes/add_note'.format(application_id)
    }

    return render_template("view_interview_details.html", general_details=general_details, interview_details=interview_details)
