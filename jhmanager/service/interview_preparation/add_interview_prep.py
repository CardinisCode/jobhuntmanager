from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_specific_interview


def display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    interview = interviewsRepo.getInterviewByID(interview_id)
    company = companyRepo.getCompanyById(application.company_id)
    interview_prep_entries = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)

    company_details = {}
    company_details["fields"]= {
        "name": company.name, 
        "description": company.description, 
        "website": company.url, 
        "interviewers": interview.interviewer_names, 
    }
    cleanup_specific_company(company_details)

    application_details = {}
    application_details["fields"] = {
        "job_role": application.job_role, 
        "job_description": application.job_description, 
        "interview_stage": application.interview_stage     
    }
    cleanup_specific_job_application(application_details)

    interview_details = {}
    interview_details["fields"] = {
        "date": interview.interview_date, 
        "time": interview.interview_time, 
        "status": interview.status, 
        "interview_type": interview.interview_type,
    }
    cleanup_specific_interview(interview_details, interview.other_medium)

    interview_prep_details = {
        "fields": None, 
        "empty_table": True
    }

    # If there are any interview_prep entries to display, lets add them to our dict:
    question_number = 0
    if interview_prep_entries: 
        interview_prep_details["fields"] = {}
        interview_prep_details["empty_table"] = False 
        for entry in interview_prep_entries: 
            question_number += 1
            prep_id = entry.interview_prep_id
            view_prep_entry = '/applications/{}/interview/{}/interview_preparation/{}/view_interview_prep_entry'.format(application_id, interview_id, prep_id)
            interview_prep_details["fields"][prep_id] = {
                "Question": entry.question,
                "Answer": replace_na_value_with_none(entry.answer), 
                "question_number": question_number,
                "view_prep_entry": view_prep_entry,
            }

    view_all_interview_prep = '/applications/{}/interview/{}/view_all_preparation'.format(application_id, interview_id)
    links = {
        "application_id": application_id,
        "interview_id": interview_id,
        "action_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id), 
        "view_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_all_interview_prep": view_all_interview_prep,
        "view_company_profile": '/company/{}/view_company'.format(company.company_id), 
        "view_company_notes": '/company/{}/view_all_company_notes'.format(company.company_id),
        "glassdoor": "https://www.glassdoor.co.uk/blog/50-common-interview-questions/", 
        "the_muse": "https://www.themuse.com/advice/interview-questions-and-answers", 
        "monster": "https://www.monster.com/career-advice/article/100-potential-interview-questions", 
        "national_careers_service_UK": "https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions" 
    }

    general_details = {
        "interview_prep_details": interview_prep_details,
        "company_details": company_details, 
        "application_details": application_details, 
        "interview_details": interview_details,
        "links": links,
    }

    return render_template("interview_prep.html", general_details=general_details, interview_prep_form=interview_prep_form)


def post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, interviewPrepRepo):
    form_details = {
        "user_id": user_id,
        "application_id": application_id,
        "interview_id": interview_id,
        "question_data": interview_prep_form.question.data, 
        "answer_data": interview_prep_form.answer.data,
    }

    interviewPrepRepo.createInterviewPreparation(form_details)
    
    flash("Interview Preparation entry saved successfully.")

    redirect_url = "/applications/{}/interview/{}/interview_preparation".format(application_id, interview_id)
    return redirect(redirect_url)