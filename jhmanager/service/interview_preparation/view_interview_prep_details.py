from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_specific_interview


def display_interview_prep_details(application_id, interview_id, interview_prep_id, interviewPrepRepo, applicationsRepo, companyRepo, interviewsRepo):
    interview_prep = interviewPrepRepo.getInterviewPrepByID(interview_prep_id)
    application = applicationsRepo.getApplicationByID(application_id)
    interview = interviewsRepo.getInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    interview_prep_details = {}
    interview_prep_details["fields"] = {
        "prep_id": interview_prep.interview_prep_id, 
        "question": interview_prep.question,
        "answer": interview_prep.answer
    }

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
    }
    cleanup_specific_job_application(application_details)

    interview_details = {}
    interview_details["fields"] = {
        "date": interview.interview_date, 
        "time": interview.interview_time, 
        "interview_type": interview.interview_type, 
        "status": interview.status,
        "other_medium": interview.other_medium
    }
    cleanup_specific_interview(interview_details, interview_details["fields"]["other_medium"])

    update_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    delete_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/delete_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    links = {
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "company_website": company.url,
        "view_application": '/applications/{}'.format(application.app_id), 
        "view_interview": '/applications/{}/interview/{}'.format(application.app_id, interview.interview_id),
        "update_prep": update_prep_link,
        "view_all_interview_prep": '/applications/{}/interview/{}/view_all_preparation'.format(application.app_id, interview.interview_id),
        "delete_prep": delete_prep_link, 
        "add_interview_prep": '/applications/{}/interview/{}/interview_preparation'.format(application.app_id, interview.interview_id)
    }

    general_details = {
        "links": links,
        "interview_prep_details": interview_prep_details,
        "company_details": company_details,
        "application_details": application_details, 
        "interview_details": interview_details
    }

    return render_template("view_interview_prep_details.html", general_details=general_details)