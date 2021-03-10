from flask import Flask, render_template, session, request, redirect, flash


def display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo):
    interview_prep_entries = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)
    interview_prep_details = None 

    question_number = 0

    if interview_prep_entries: 
        interview_prep_details = {} 
        for entry in interview_prep_entries: 
            question_number += 1
            prep_id = entry.interview_prep_id
            interview_prep_details[prep_id] = {
                "Question": entry.question,
                "Answer": entry.answer, 
                "Q#": question_number
            }
    
    details = {
        "application_id": application_id,
        "interview_id": interview_id,
    }

    return render_template("interview_prep.html", interview_prep_form=interview_prep_form, details=details, interview_prep_details=interview_prep_details)


def post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, applicationsRepo, interviewPrepRepo):
    question_data = interview_prep_form.interview_question.data
    answer_data = interview_prep_form.answer_text.data

    form_details = {
        "user_id": user_id,
        "application_id": application_id,
        "interview_id": interview_id,
        "question_data": question_data, 
        "answer_data": answer_data,
    }

    interviewPrepRepo.addInterviewPrep(form_details)
    
    flash("Details added to DB.")

    # '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'
    redirect_url = "/applications/{}/interview/{}/interview_preparation".format(application_id, interview_id)
    return redirect(redirect_url)