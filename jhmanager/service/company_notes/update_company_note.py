from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, date


def display_update_company_note_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo):
    company = companyRepo.getCompanyById(company_id)
    details = {
        "company_name": company.name,
        "action_url": '/company/{}/company_note/{}/update_note'.format(company_id, company_note_id),
    }

    return render_template("update_company_note.html", details=details, update_note_form=update_note_form)


def post_update_company_form(update_note_form, company_id, company_note_id, companyNotesRepo):
    entry_date = datetime.now().date()
    date_format = "%Y-%m-%d"
    entry_date_str = entry_date.strftime(date_format)
    
    details = {
        "date": entry_date_str, 
        "subject": update_note_form.subject.data, 
        "note_text": update_note_form.note_text.data, 
        "company_note_id": company_note_id
    }
    companyNotesRepo.UpdateCompanyNoteByID(details)

    flash("Note ID #{} has been updated successfully!".format(company_note_id))
    redirect_url = '/company/{}/company_note/{}/view_note_details'.format(company_id, company_note_id)
    return redirect(redirect_url)