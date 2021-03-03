from flask import Flask, render_template, session, request, redirect


def display_user_note_details(application_id, note_id, userNotesRepo, companyRepo):
    user_notes = userNotesRepo.getUserNotesByID(application_id, note_id)
    company_id = user_notes.company_id
    company_name = companyRepo.getCompanyById(company_id).name
    update_url =  "/applications/{}/user_notes/{}/update_note".format(application_id, note_id)
    delete_note_url = "/applications/{}/user_notes/{}/delete_note".format(application_id, note_id)

    general_details = {
        "application_id": application_id,
    }

    note_details = {
        "note_id": user_notes.notes_id,
        "Date": user_notes.entry_date,
        "company_name": company_name,
        "Subject": user_notes.description, 
        "Note": user_notes.user_notes, 
        "update_url": update_url,
        "delete_note_url": delete_note_url
    }

    return render_template("view_notes_details.html", note_details=note_details, general_details=general_details)