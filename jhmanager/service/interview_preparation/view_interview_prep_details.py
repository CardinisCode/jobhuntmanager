from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none


def display_interview_prep_details(application_id, interview_id, interview_prep_id, interviewPrepRepo, applicationsRepo, companyRepo, interviewsRepo):
    interview_prep = interviewPrepRepo.getEntryByInterviewPrepID(interview_prep_id)
    application = applicationsRepo.grabApplicationByID(application_id)
    interview = interviewsRepo.grabInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)

    general_details = {
        "interview_prep_details": {}, 
        "company_details": {}, 
        "application_details": {}, 
        "interview_details" : {},
        "links": {}
    }

    general_details["interview_prep_details"] = {
        "prep_id": interview_prep.interview_prep_id, 
        "question": interview_prep.question,
        "answer": interview_prep.answer
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description),
        "location": replace_na_value_with_none(company.location),
        "industry": replace_na_value_with_none(company.industry), 
    }

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "job_description": replace_na_value_with_none(application.job_description), 
        "interview_stage": application.interview_stage,
    }

    general_details["interview_details"] = {
        "date": cleanup_date_format(interview.interview_date), 
        "time": cleanup_time_format(interview.interview_time), 
        "interview_type": cleanup_interview_type(interview.interview_type),
        "status": cleanup_interview_status(interview.status)
    }

    update_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    delete_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/delete_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    view_interview = '/applications/{}/interview/{}'.format(application.app_id, interview.interview_id)
    view_all_interview_prep = '/applications/{}/interview/{}/view_all_preparation'.format(application.app_id, interview.interview_id)
    general_details["links"] = {
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "company_website": company.url,
        "view_application": '/applications/{}'.format(application.app_id), 
        "view_interview": view_interview,
        "update_prep": update_prep_link,
        "view_all_interview_prep": view_all_interview_prep,
        "delete_prep": delete_prep_link, 
    }


    return render_template("view_interview_prep_details.html", general_details=general_details)