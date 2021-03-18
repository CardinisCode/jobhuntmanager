from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_app_note_form(application_id, user_id, app_notes_id, update_app_note_form, companyRepo, appNotesRepo):
    company_id = appNotesRepo.getNoteByAppNoteID(app_notes_id).company_id
    company_name = companyRepo.getCompanyById(company_id).name
    update_url = '/applications/{}/app_notes/{}/update_note'.format(application_id, app_notes_id)

    details = {
        "company_name": company_name,
        "application_id": application_id,
        "note_id": app_notes_id,
        "update_url": update_url
    }

    return render_template("update_application_note.html", update_note_form=update_app_note_form, details=details)


def post_update_app_note(update_app_note_form, appNotesRepo, app_notes_id, application_id):
    details = {
        "description": update_app_note_form.description.data, 
        "notes_text": update_app_note_form.notes_text.data,
        "note_id": app_notes_id
    }

    message = appNotesRepo.updateByID(details)

    redirect_url = '/applications/{}/app_notes/{}/view_note'.format(application_id, app_notes_id)
    flash(message)
    return redirect(redirect_url)

