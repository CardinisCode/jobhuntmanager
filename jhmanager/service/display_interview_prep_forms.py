from flask import Flask, render_template, session, request, redirect


def display_interview_prep(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo):
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