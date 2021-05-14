from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none


def display_all_interviews_for_application(application_id, interviewsRepo, companyRepo, applicationsRepo):
    interviews_list = interviewsRepo.getInterviewsByApplicationID(application_id)
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    
    general_details = {
        "links": {}, 
        "company_name": company.name,
        "application_details": {}, 
        "company_details": {}
    }

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "interview_stage": cleanup_interview_stage(application.interview_stage), 
        "employment_type": cleanup_emp_type_field(application.employment_type)
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description), 
        "location": replace_na_value_with_none(company.location)
    }

    general_details["links"] = {
        "add_new_interview": '/applications/{}/add_interview'.format(application_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_company_profile": '/company/{}/view_company'.format(company.company_id)
    }

    interview_details = None
    if interviews_list:
        interview_details = {"fields": {}}
        for interview in interviews_list:
            interview_id = interview.interview_id
            view_interview = '/applications/{}/interview/{}'.format(application_id, interview_id)
            interview_details["fields"][interview_id] = {
                "date": cleanup_date_format(interview.interview_date), 
                "time": cleanup_time_format(interview.interview_time),
                "interview_type": cleanup_interview_type(interview.interview_type),
                "status": cleanup_interview_status(interview.status),
                "view_interview": view_interview
            }


    return render_template("view_all_interviews.html", general_details=general_details, interview_details=interview_details)