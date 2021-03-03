from flask import Flask, render_template, session, request, redirect

def display_all_user_notes(user_id, userNotesRepo, companyRepo):
    note_details = {}
    general_details = {}
    
    user_notes = userNotesRepo.getUserNotesByUserId(user_id)

    if not user_notes:
        general_details["empty_table"] = True
        general_details["message"] = "Start adding notes."
    
    else: 
        note_id = 0
        for note in user_notes:
            note_id += 1
            general_details["message"] = "View table below..."
            general_details["empty_table"] = False
            company_id = note.company_id
            company_name = companyRepo.getCompanyById(company_id).name
            application_id = note.application_id

            note_details[note_id] = {
                "note_id": note.notes_id,
                "entry_date": note.entry_date,
                "company_name": company_name,
                "description": note.description, 
                "note_text": note.user_notes, 
                "application_id": application_id, 
                "company_id": company_id, 
                "view_more": "/applications/{}/user_notes/{}".format(application_id, note.notes_id), 
                "delete_url": '/applications/{}/user_notes/{}/delete_note'.format(application_id, note.notes_id)
            }

    return render_template("view_all_user_notes.html", general_details=general_details, note_details=note_details)