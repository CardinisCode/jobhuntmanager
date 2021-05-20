from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_specific_interview
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none


def display_all_interview_prep_entries(application_id, interview_id, user_id, applicationsRepo, interviewsRepo, interviewPrepRepo, companyRepo):
    interview_prep_list = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)
    application = applicationsRepo.getApplicationByID(application_id)
    interview = interviewsRepo.getInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    application_details = {}
    application_details["fields"] = {
        "job_role": application.job_role, 
        "employment_type": application.employment_type,  
        "interview_stage": application.interview_stage,
    }
    cleanup_specific_job_application(application_details)

    company_details = {}
    company_details["fields"] = {
        "name": company.name, 
        "description": company.description,
        "location": company.location,
        "industry": company.industry, 
    }
    cleanup_specific_company(company_details)

    interview_details = {}
    interview_details["fields"] = {
        "date": interview.interview_date, 
        "time": interview.interview_time, 
        "interview_type": interview.interview_type,
        "status": interview.status,
    }
    cleanup_specific_interview(interview_details, interview.other_medium)

    interview_prep_details = None

    if interview_prep_list: 
        interview_prep_details = {}
        interview_prep_details["fields"] = {}
        count = 0
        for prep in interview_prep_list:
            count += 1
            interview_prep_id = prep.interview_prep_id
            view_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/view_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
            interview_prep_details["fields"][interview_prep_id] = {
                "number": count, 
                "question": prep.question, 
                "answer": replace_na_value_with_none(prep.answer), 
                "view_prep_link": view_prep_link
            }

    add_interview_prep = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    view_interview = '/applications/{}/interview/{}'.format(application.app_id, interview.interview_id)
    links = {
        "add_interview_prep": add_interview_prep,
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "view_application": '/applications/{}'.format(application.app_id), 
        "view_interview": view_interview,
    }

    general_details = {
        "interview_prep_details": interview_prep_details, 
        "interview_details": interview_details, 
        "company_details": company_details, 
        "application_details": application_details,
        "links": links
    }

    return render_template("view_all_interview_prep.html", general_details=general_details)