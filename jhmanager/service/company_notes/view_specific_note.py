from flask import Flask, render_template, session, request, redirect, flash


def display_company_note_details(company_id, company_note_id, companyRepo, companyNotesRepo, user_id):
    company = companyRepo.getCompanyById(company_id)
    note_details = companyNotesRepo.getCompanyNoteByID(company_note_id)
    details = {
        "company_name": company.name,
        "company_notes_url": '/company/{}/view_all_company_notes'.format(company_id),
        "company_profile_url": '/company/{}/view_company'.format(company_id), 
        "date": note_details.entry_date, 
        "subject": note_details.subject, 
        "note_text": note_details.note_text
    }

    return render_template("view_specific_company_note.html", details=details)