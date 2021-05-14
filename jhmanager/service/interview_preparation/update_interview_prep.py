from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status


def display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo, interviewsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    interview = interviewsRepo.getInterviewByID(interview_id)

    general_details = {
        "company_details": {}, 
        "application_details": {},
        "interview_details": {}, 
        "links": {}
    }

    general_details["company_details"] = {
        "name": company.name, 
        "description": replace_na_value_with_none(company.description), 
        "location": replace_na_value_with_none(company.location), 
        "interviewers": replace_na_value_with_none(interview.interviewer_names)
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

    view_all_interview_prep = '/applications/{}/interview/{}/view_all_preparation'.format(application_id, interview_id)
    general_details["links"] = {
        "action_url": '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id),
        "view_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "view_application": '/applications/{}'.format(application_id), 
        "view_all_interview_prep": view_all_interview_prep,
        "glassdoor": "https://www.glassdoor.co.uk/blog/50-common-interview-questions/", 
        "the_muse": "https://www.themuse.com/advice/interview-questions-and-answers", 
        "monster": "https://www.monster.com/career-advice/article/100-potential-interview-questions", 
        "national_careers_service_UK": "https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions" 
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