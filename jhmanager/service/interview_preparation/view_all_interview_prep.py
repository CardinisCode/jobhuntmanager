from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_emp_type_field


def display_all_interview_prep_entries(application_id, interview_id, user_id, applicationsRepo, interviewsRepo, interviewPrepRepo, companyRepo):
    interview_prep_list = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)
    application = applicationsRepo.grabApplicationByID(application_id)
    interview = interviewsRepo.grabInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    general_details = {
        "interview_prep_details": None, 
        "interview_details": {}, 
        "company_details": {}, 
        "application_details": {},
        "links": {}
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description),
        "location": replace_na_value_with_none(company.location),
        "industry": replace_na_value_with_none(company.industry), 
    }

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "employment_type": cleanup_emp_type_field(application.employment_type),  
        "interview_stage": cleanup_interview_stage(application.interview_stage),
    }

    general_details["interview_details"] = {
        "date": cleanup_date_format(interview.interview_date), 
        "time": cleanup_time_format(interview.interview_time), 
        "interview_type": cleanup_interview_type(interview.interview_type),
        "status": cleanup_interview_status(interview.status)
    }

    if interview_prep_list: 
        general_details["interview_prep_details"] = {}
        general_details["interview_prep_details"]["fields"] = {}
        count = 0
        for prep in interview_prep_list:
            count += 1
            interview_prep_id = prep.interview_prep_id
            view_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/view_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
            general_details["interview_prep_details"]["fields"][interview_prep_id] = {
                "number": count, 
                "question": prep.question, 
                "answer": prep.answer, 
                "view_prep_link": view_prep_link
            }

    add_interview_prep = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    view_interview = '/applications/{}/interview/{}'.format(application.app_id, interview.interview_id)
    general_details["links"] = {
        "add_interview_prep": add_interview_prep,
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "view_application": '/applications/{}'.format(application.app_id), 
        "view_interview": view_interview,

    }

    return render_template("view_all_interview_prep.html", general_details=general_details)