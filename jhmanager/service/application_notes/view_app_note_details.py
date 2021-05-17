from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_field_value
from datetime import datetime, time


def display_application_note_details(application_id, app_notes_id, appNotesRepo, companyRepo):
    app_note_entry = appNotesRepo.getNoteByAppNoteID(app_notes_id)
    company = companyRepo.getCompanyById(app_note_entry.company_id)

    general_details = {
        "links": {}, 
        "note_details": {}
    }

    general_details["links"] = {
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "all_app_notes": '/applications/{}/view_application_notes'.format(application_id),
        "view_application": '/applications/{}'.format(application_id),
        "update_note": '/applications/{}/app_notes/{}/update_note'.format(application_id, app_notes_id), 
        "delete_note": "/applications/{}/app_notes/{}/delete_note".format(application_id, app_notes_id), 
        "add_new_note": '/applications/{}/app_notes/add_note'.format(application_id)
    }

    note_date_obj = datetime.strptime(app_note_entry.entry_date, "%Y-%m-%d")

    general_details["note_details"] = {
        "note_id": app_note_entry.app_notes_id,
        "date": cleanup_date_format(note_date_obj),
        "company_name": cleanup_field_value(company.name),
        "subject": cleanup_field_value(app_note_entry.description), 
        "note": app_note_entry.notes_text, 
    }

    return render_template("view_app_note_details.html", general_details=general_details)