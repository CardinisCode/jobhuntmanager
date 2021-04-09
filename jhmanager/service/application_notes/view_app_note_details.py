from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from datetime import datetime, time


def display_application_note_details(application_id, app_notes_id, appNotesRepo, companyRepo):
    app_notes = appNotesRepo.getNoteByAppNoteID(app_notes_id)
    company_id = app_notes.company_id
    company = companyRepo.getCompanyById(company_id)

    general_details = {
        "links": {}, 
        "note_details": {}
    }

    general_details["links"] = {
        "company_profile": '/company/{}/view_company'.format(company_id),
        "all_app_notes": '/applications/{}/view_application_notes'.format(application_id),
        "view_application": '/applications/{}'.format(application_id),
        "update_note": '/applications/{}/app_notes/{}/update_note'.format(application_id, app_notes_id), 
        "delete_note": "/applications/{}/app_notes/{}/delete_note".format(application_id, app_notes_id), 
        "add_new_note": '/applications/{}/app_notes/add_note'.format(application_id)
    }

    note_date_obj = datetime.strptime(app_notes.entry_date, "%Y-%m-%d")

    general_details["note_details"] = {
        "note_id": app_notes.app_notes_id,
        "date": cleanup_date_format(note_date_obj),
        "company_name": company.name,
        "subject": app_notes.description, 
        "note": app_notes.notes_text, 
    }

    return render_template("view_app_note_details.html", general_details=general_details)