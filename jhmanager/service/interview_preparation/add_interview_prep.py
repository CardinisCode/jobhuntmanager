from flask import Flask, render_template, session, request, redirect, flash


def display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo):
    company_id = applicationsRepo.grabApplicationByID(application_id).company_id
    interview = interviewsRepo.grabInterviewByID(interview_id)
    company = companyRepo.getCompanyById(company_id)
    company_details = {
        "company_name": company.name, 
        "description": company.description, 
        "location": company.location, 
        "website": company.url, 
        "interviewers": interview.interviewer_names, 
        "view_profile": '/company/{}/view_company'.format(company_id), 
        "view_notes": '/company/{}/view_all_company_notes'.format(company_id)
    }
    company_name = companyRepo.getCompanyById(company_id).name
    
    interview_prep_entries = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)
    interview_prep_details = None 

    question_number = 0

    if interview_prep_entries: 
        interview_prep_details = {} 
        for entry in interview_prep_entries: 
            question_number += 1
            prep_id = entry.interview_prep_id
            update_prep_entry = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, prep_id)
            delete_prep_entry = '/applications/{}/interview/{}/interview_preparation/{}/delete_interview_prep_entry'.format(application_id, interview_id, prep_id)
            interview_prep_details[prep_id] = {
                "Question": entry.question,
                "Answer": entry.answer, 
                "question_number": question_number,
                "update_prep_entry": update_prep_entry,
                "delete_prep_entry": delete_prep_entry
            }
    
    details = {
        "application_id": application_id,
        "interview_id": interview_id,
        "action_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id), 
        "return_to_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "return_to_application": '/applications/{}'.format(application_id), 
        "company_name": company_name
    }

    links = {
        "glassdoor": "https://www.glassdoor.co.uk/blog/50-common-interview-questions/", 
        "the_muse": "https://www.themuse.com/advice/interview-questions-and-answers", 
        "monster": "https://www.monster.com/career-advice/article/100-potential-interview-questions", 
        "national_careers_service_UK": "https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions" 
    }

    return render_template("interview_prep.html", interview_prep_form=interview_prep_form, details=details, interview_prep_details=interview_prep_details, company_details=company_details, links=links)


def post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, applicationsRepo, interviewPrepRepo):
    question_data = interview_prep_form.question
    answer_data = interview_prep_form.answer_text.data

    form_details = {
        "user_id": user_id,
        "application_id": application_id,
        "interview_id": interview_id,
        "question_data": interview_prep_form.question.data, 
        "answer_data": interview_prep_form.answer.data,
    }

    interviewPrepRepo.addInterviewPrep(form_details)
    
    flash("Details added to DB.")

    # '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'
    redirect_url = "/applications/{}/interview/{}/interview_preparation".format(application_id, interview_id)
    return redirect(redirect_url)