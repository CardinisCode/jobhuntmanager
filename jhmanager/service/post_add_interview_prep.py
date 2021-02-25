from flask import Flask, render_template, session, request, redirect, flash


def post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, applicationsRepo, interviewPrepRepo):
    question_data = interview_prep_form.interview_question.data
    answer_data = interview_prep_form.answer_text.data

    form_details = {
        "user_id": user_id,
        "interview_id": interview_id,
        "question_data": question_data, 
        "answer_data": answer_data,
    }

    interviewPrepRepo.addInterviewPrep(form_details)
    
    flash("Details added to DB.")

    # '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'
    redirect_url = "/applications/{}/interview/{}/interview_preparation".format(application_id, interview_id)
    return redirect(redirect_url)