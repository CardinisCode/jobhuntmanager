from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, date


def display_user_notes_form(notes_form, application_id, companyRepo, applicationsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "application_id": application.app_id,
        "company_name": company.name
    }

    return render_template("add_notes.html", notes_form=notes_form, details=details)


def post_add_note(notes_form, application_id, user_id, userNotesRepo, applicationsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company_id = application.company_id

    date_of_entry = datetime.now().date()
    date_format = "%Y-%m-%d"
    entry_date_str = date_of_entry.strftime(date_format)

    details = {
        "user_id": user_id, 
        "application_id": application_id, 
        "company_id": company_id,
        "date_of_entry": entry_date_str,
        "description": notes_form.description.data, 
        "notes_text": notes_form.user_notes.data
    }

    userNotesRepo.insertNewNotes(details)

    redirect_url = '/applications/{}'.format(application_id)
    flash("Notes successfully saved.")
    return redirect(redirect_url)