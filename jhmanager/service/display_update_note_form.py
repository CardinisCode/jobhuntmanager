from flask import Flask, render_template, session, request, redirect
from jhmanager.forms.add_notes_form import AddNotesForm


def display_update_user_note_form(application_id, user_id, note_id, update_note_form, companyRepo, userNotesRepo):
    company_id =  userNotesRepo.getUserNotesForApplication(application_id, user_id)[0].company_id
    company_name = companyRepo.getCompanyById(company_id).name
    update_url = '/applications/{}/user_notes/{}/update_note'.format(application_id, note_id)

    details = {
        "company_name": company_name,
        "update_url": update_url
    }

    return render_template("update_user_note.html", update_note_form=update_note_form, details=details)

