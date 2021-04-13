
from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from datetime import datetime, date


def display_application_notes(user_id, application_id, applicationsRepo, appNotesRepo, companyRepo):
    application_notes = appNotesRepo.getAppNotesByApplicationID(application_id, user_id)
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    links = {
        "add_note": '/applications/{}/app_notes/add_note'.format(application_id), 
        "view_application": '/applications/{}'.format(application_id), 
        "company_profile": '/company/{}/view_company'.format(company.company_id)
    }

    company_details = {
        "name": company.name
    }

    user_notes_details = {
        "empty_table": True,
        "fields": None
    }

    if application_notes:
        note_count = 0
        user_notes_details["empty_table"] = False
        user_notes_details["fields"] = {}
        for note in application_notes:
            note_count += 1
            note_id = note.app_notes_id
            entry_date_obj = datetime.strptime(note.entry_date, "%Y-%m-%d")
            note_text = note.notes_text[0:20] + "....."    
            user_notes_details["fields"][note_count] = {
                "note_id": note_id,
                "entry_date": cleanup_date_format(entry_date_obj), 
                "subject": note.description, 
                "note_text": note_text, 
                "view_note": '/applications/{}/app_notes/{}/view_note'.format(application_id, note_id), 
            }

    general_details = {
        "links": links, 
        "company": company_details, 
        "user_notes_details": user_notes_details
    }

    return render_template("view_notes_for_application.html", general_details=general_details)