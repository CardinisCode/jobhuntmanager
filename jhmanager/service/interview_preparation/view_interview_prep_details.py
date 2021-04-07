from flask import Flask, render_template, session, request, redirect, flash


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
        "description": company.description,
        "location": company.location,
        "industry": company.industry
    }

    general_details["application_details"] = {
        "job_role": application.job_role, 
        "job_description": application.job_description, 
        "interview_stage": application.interview_stage,
    }

    general_details["interview_details"] = {
        "date": interview.interview_date, 
        "time": interview.interview_time, 
        "interviewers": interview.interviewer_names,
    }

    update_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    delete_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/delete_interview_prep_entry'.format(application.app_id, interview.interview_id, interview_prep.interview_prep_id)
    view_interview = '/applications/{}/interview/{}'.format(application.app_id, interview.interview_id)
    general_details["links"] = {
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "company_website": company.url,
        "view_application": '/applications/{}'.format(application.app_id), 
        "view_interview": view_interview,
        "update_prep": update_prep_link,
        "delete_prep": delete_prep_link
    }


    return render_template("view_interview_prep_details.html", general_details=general_details)