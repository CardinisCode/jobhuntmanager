from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none


def display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    interview = interviewsRepo.grabInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)
    company_id = company.company_id
    interview_prep_entries = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)

    general_details = {
        "interview_prep_details": None,
        "company_details": {}, 
        "application_details": {}, 
        "interview_details": {},
        "links": {},
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description), 
        "location": replace_na_value_with_none(company.location), 
        "website": company.url, 
        "interviewers": interview.interviewer_names, 
        "view_profile": '/company/{}/view_company'.format(company_id), 
        "view_notes": '/company/{}/view_all_company_notes'.format(company_id)
    }
    

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "job_description": replace_na_value_with_none(application.job_description), 
        "interview_stage": cleanup_interview_stage(application.interview_stage)
    }

    general_details["interview_details"] = {
        "date": cleanup_date_format(interview.interview_date), 
        "time": cleanup_time_format(interview.interview_time), 
        "status": cleanup_interview_status(interview.status), 
        "interview_type": cleanup_interview_type(interview.interview_type)
    }

    # If there are any interview_prep entries to display, lets add them to our dict:
    question_number = 0
    if interview_prep_entries: 
        general_details["interview_prep_details"] = {}
        general_details["interview_prep_details"]["fields"] = {}
        interview_prep_details = {} 
        for entry in interview_prep_entries: 
            question_number += 1
            prep_id = entry.interview_prep_id
            view_prep_entry = '/applications/{}/interview/{}/interview_preparation/{}/view_interview_prep_entry'.format(application_id, interview_id, prep_id)
            general_details["interview_prep_details"]["fields"][prep_id] = {
                "Question": entry.question,
                "Answer": replace_na_value_with_none(entry.answer), 
                "question_number": question_number,
                "view_prep_entry": view_prep_entry,
            }

    view_all_interview_prep = '/applications/{}/interview/{}/view_all_preparation'.format(application_id, interview_id)
    general_details["links"] = {
        "application_id": application_id,
        "interview_id": interview_id,
        "action_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id), 
        "view_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_all_interview_prep": view_all_interview_prep,
        "glassdoor": "https://www.glassdoor.co.uk/blog/50-common-interview-questions/", 
        "the_muse": "https://www.themuse.com/advice/interview-questions-and-answers", 
        "monster": "https://www.monster.com/career-advice/article/100-potential-interview-questions", 
        "national_careers_service_UK": "https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions" 
    }

    return render_template("interview_prep.html", general_details=general_details, interview_prep_form=interview_prep_form)


def post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, applicationsRepo, interviewPrepRepo):
    form_details = {
        "user_id": user_id,
        "application_id": application_id,
        "interview_id": interview_id,
        "question_data": interview_prep_form.question.data, 
        "answer_data": interview_prep_form.answer.data,
    }

    interviewPrepRepo.createInterviewPreparation(form_details)
    
    flash("Interview Preparation entry saved successfully.")

    # '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'
    redirect_url = "/applications/{}/interview/{}/interview_preparation".format(application_id, interview_id)
    return redirect(redirect_url)