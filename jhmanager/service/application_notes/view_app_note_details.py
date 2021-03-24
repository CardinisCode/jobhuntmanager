from flask import Flask, render_template, session, request, redirect


def display_application_note_details(application_id, app_notes_id, appNotesRepo, companyRepo):
    app_notes = appNotesRepo.getNoteByAppNoteID(app_notes_id)
    company_id = app_notes.company_id
    company_name = companyRepo.getCompanyById(company_id).name
    update_url =  '/applications/{}/app_notes/{}/update_note'.format(application_id, app_notes_id)
    delete_note_url = "/applications/{}/app_notes/{}/delete_note".format(application_id, app_notes_id)
    company_profile = '/company/{}/view_company'.format(company_id)
    all_app_notes = '/applications/{}/view_application_notes'.format(application_id)
    view_application = '/applications/{}'.format(application_id)

    general_details = {
        "application_id": application_id,
        "company_profile": company_profile,
        "all_app_notes": all_app_notes,
        "view_application": view_application
    }

    note_details = {
        "note_id": app_notes.app_notes_id,
        "Date": app_notes.entry_date,
        "company_name": company_name,
        "Subject": app_notes.description, 
        "Note": app_notes.notes_text, 
        "update_url": update_url,
        "delete_note_url": delete_note_url
    }

    return render_template("view_app_note_details.html", note_details=note_details, general_details=general_details)