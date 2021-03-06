from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_specific_company
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_specific_job_application
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_specific_interview


def display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo, interviewsRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    interview = interviewsRepo.getInterviewByID(interview_id)

    application_details = {}
    application_details["fields"] = {
        "job_role": application.job_role, 
        "job_description": application.job_description, 
        "interview_stage": application.interview_stage
    }
    cleanup_specific_job_application(application_details)

    company_details = {}
    company_details["fields"] = {
        "name": company.name, 
        "description": company.description, 
        "location": company.location, 
        "interviewers": company.interviewer_names
    }
    cleanup_specific_company(company_details)

    interview_details = {}
    interview_details["fields"] = {
        "date": interview.interview_date,
        "time": interview.interview_time,
        "status": interview.status, 
        "interview_type": interview.interview_type,
    }
    cleanup_specific_interview(interview_details, interview.other_medium)

    view_all_interview_prep = '/applications/{}/interview/{}/view_all_preparation'.format(application_id, interview_id)
    links = {
        "action_url": '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id),
        "view_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_all_interview_prep": view_all_interview_prep,
        "glassdoor": "https://www.glassdoor.co.uk/blog/50-common-interview-questions/", 
        "the_muse": "https://www.themuse.com/advice/interview-questions-and-answers", 
        "monster": "https://www.monster.com/career-advice/article/100-potential-interview-questions", 
        "national_careers_service_UK": "https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions" 
    }

    general_details = {
        "company_details": company_details, 
        "application_details": application_details,
        "interview_details": interview_details, 
        "links": links
    }

    return render_template("update_interview_prep.html", general_details=general_details, update_interview_prep_form=update_interview_prep_form)


def post_update_interview_preparation(application_id, interview_id, interview_prep_id, update_interview_prep_form, interviewPrepRepo):
    prep_fields = {
        "specific_question": update_interview_prep_form.question.data, 
        "specific_answer": update_interview_prep_form.answer.data, 
        "interview_prep_id": interview_prep_id
    }

    for heading, value in prep_fields.items():
        if value == "":
            prep_fields[heading] = "N/A"

    output = interviewPrepRepo.updateInterviewPrepByID(prep_fields)
    if not output: 
        flash("Failed to update the details. Please try again.")
        redirect_url = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
        return redirect(redirect_url)

    flash("Details for this interview preparation entry have been updated successfully.")

    redirect_url = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    return redirect(redirect_url)