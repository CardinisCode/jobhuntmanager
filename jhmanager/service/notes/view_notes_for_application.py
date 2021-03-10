
from flask import Flask, render_template, session, request, redirect


def display_all_user_notes_for_application(user_id, application_id, applicationsRepo, userNotesRepo, companyRepo):
    application_notes = userNotesRepo.getUserNotesForApplication(application_id, user_id)
    company_id = applicationsRepo.grabApplicationByID(application_id).company_id
    add_note_url = "/applications/{}/add_notes".format(application_id)

    general_details = {
        "company_id": company_id, 
        "company_name": companyRepo.getCompanyById(company_id).name,
        "application_id": application_id,
        "add_note_url": add_note_url
    }

    user_notes_details = None

    if not application_notes:
        general_details["empty_table"] = True

    else:
        note_count = 0
        general_details["empty_table"] = False
        user_notes_details = {} 
        for note in application_notes:
            note_count += 1
            note_id = note.notes_id
            view_note_url = "/applications/{}/user_notes/{}".format(application_id, note_id)
            delete_url = "/applications/{}/user_notes/{}/delete_note".format(application_id, note_id)
            user_notes_details[note_count] = {
                "note_id": note_id,
                "entry_date": note.entry_date, 
                "subject": note.description, 
                "note_text": note.user_notes, 
                "view_note_url": view_note_url,
                "delete_url": delete_url
            }

    return render_template("view_notes_for_application.html", general_details=general_details, user_notes_details=user_notes_details)