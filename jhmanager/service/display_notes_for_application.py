
from flask import Flask, render_template, session, request, redirect


def display_all_user_notes_for_application(user_id, application_id, userNotesRepo, companyRepo):
    application_notes = userNotesRepo.getUserNotesForApplication(application_id, user_id)

    user_notes_details = None
    general_details = {}
    if not application_notes:
        general_details["empty_table"] = True
        general_details["message"] = "Start Adding notes now..."

    else:
        raise ValueError("Details below...")
    
    # general_details = {
    #     "company_name": companyRepo.getCompanyById(company_id).name, 
    #     "company_id": company_id, 
    #     "message": ""
    # }


    # else:
    #     note_count = 0
    #     user_notes_details = {}
    #     for note in company_notes:
    #         note_count += 1
    #         user_notes_details[note_count] = {
    #             "entry_date": note.entry_date,
    #             "subject": note.description,
    #             "note_text": note.user_notes, 
    #         }

    return render_template("view_notes_for_application.html", general_details=general_details, user_notes_details=user_notes_details)