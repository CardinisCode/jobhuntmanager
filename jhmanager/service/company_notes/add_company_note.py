from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, date


def display_add_company_note_form(company_id, company_note_form, companyRepo):
    company = companyRepo.getCompanyById(company_id)
    details = {
        "company_name": company.name, 
        "company_id": company_id, 
        "action_url": '/company/{}/add_company_note'.format(company_id)
    }

    return render_template("add_company_note.html", company_note_form=company_note_form, details=details)


def post_add_company_note(user_id, company_id, company_note_form, companyNotesRepo): 
    subject = company_note_form.subject.data
    note_text = company_note_form.note_text.data

    entry_date = datetime.now().date()
    date_format = "%Y-%m-%d"
    entry_date_str = entry_date.strftime(date_format)

    # With these detail, lets add them to the 'company_notes' table:
    fields = {
        "user_id": user_id,
        "company_id": company_id,
        "date": entry_date_str,
        "subject": company_note_form.subject.data, 
        "note_text": company_note_form.note_text.data, 
    }
    company_note_id = companyNotesRepo.insertNewNotes(fields)

    flash("Note saved successfully!")
    redirect_url = '/company/{}/company_note/{}/view_note_details'.format(company_id, company_note_id)

    return redirect(redirect_url)