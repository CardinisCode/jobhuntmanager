from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_note_form(application_id, user_id, note_id, update_note_form, companyRepo, userNotesRepo):
    company_id =  userNotesRepo.getUserNotesForApplication(application_id, user_id)[0].company_id
    company_name = companyRepo.getCompanyById(company_id).name
    update_url = '/applications/{}/user_notes/{}/update_note'.format(application_id, note_id)

    details = {
        "company_name": company_name,
        "application_id": application_id,
        "note_id": note_id,
        "update_url": update_url
    }

    return render_template("update_user_note.html", update_note_form=update_note_form, details=details)


def post_update_note(update_note_form, userNotesRepo, note_id, application_id):
    details = {
        "description": update_note_form.description.data, 
        "notes_text": update_note_form.user_notes.data,
        "note_id": note_id
    }

    message = userNotesRepo.updateByID(details)


    redirect_url = '/applications/{}/view_notes'.format(application_id)
    flash(message)
    return redirect(redirect_url)

