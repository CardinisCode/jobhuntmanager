from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_fields


def display_all_interviews_for_application(application_id, interviewsRepo, companyRepo, applicationsRepo):
    interviews_list = interviewsRepo.getInterviewsByApplicationID(application_id)
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    application_details = {
        "job_role": application.job_role, 
        "interview_stage": application.interview_stage, 
        "employment_type": application.employment_type
    }
    cleanup_specific_job_application(application_details)

    company_details = {
        "name": company.name, 
        "description": company.description, 
        "location": company.location
    }
    cleanup_specific_company(company_details)

    links = {
        "add_new_interview": '/applications/{}/add_interview'.format(application_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_company_profile": '/company/{}/view_company'.format(company.company_id)
    }

    interview_details = None
    if interviews_list:
        interview_details = {"fields": {}}
        for interview in interviews_list:
            interview_id = interview.interview_id
            other_medium = interview.other_medium
            view_interview = '/applications/{}/interview/{}'.format(application_id, interview_id)
            interview_details["fields"][interview_id] = {
                "date": interview.interview_date, 
                "time": interview.interview_time,
                "interview_type": interview.interview_type,
                "status": interview.status,
                "view_interview": view_interview, 
            }
            cleanup_interview_fields(interview_details, interview_id, other_medium)

    general_details = {
        "links": links, 
        "application_details": application_details, 
        "company_details": company_details,
        "interview_details": interview_details
    }

    return render_template("view_all_interviews.html", general_details=general_details)