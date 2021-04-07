from flask import Flask, render_template, session, request, redirect, flash


def display_all_interview_prep_entries(application_id, interview_id, user_id, interviewPrepRepo):
    interview_prep_list = interviewPrepRepo.getAllInterviewPrepEntriesByInterviewId(interview_id, user_id)

    general_details = {
        "interview_prep_details": None, 
        "links": {}
    }

    if interview_prep_list: 
        general_details["interview_prep_details"] = {}
        general_details["interview_prep_details"]["fields"] = {}
        count = 0
        for prep in interview_prep_list:
            count += 1
            interview_prep_id = prep.interview_prep_id
            view_prep_link = '/applications/{}/interview/{}/interview_preparation/{}/view_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
            general_details["interview_prep_details"]["fields"][interview_prep_id] = {
                "number": count, 
                "question": prep.question, 
                "answer": prep.answer, 
                "view_prep_link": view_prep_link
            }

    add_interview_prep = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    general_details["links"] = {
        "add_interview_prep": add_interview_prep,
    }


    return render_template("view_all_interview_prep.html", general_details=general_details)