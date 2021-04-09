from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from datetime import datetime, time


def display_company_note_details(company_id, company_note_id, companyRepo, companyNotesRepo, user_id):
    company = companyRepo.getCompanyById(company_id)
    note_details = companyNotesRepo.getCompanyNoteByID(company_note_id)

    general_details = {
        "links": {}, 
        "note_details": {}
    }

    general_details["links"] = {
        "view_company_notes": '/company/{}/view_all_company_notes'.format(company_id),
        "view_company_profile": '/company/{}/view_company'.format(company_id), 
        "update_note": '/company/{}/company_note/{}/update_note'.format(company_id, company_note_id),
        "delete_note": '/company/{}/company_note/{}/delete_note'.format(company_id, company_note_id),
        "add_new_note": '/company/{}/add_company_note'.format(company_id)
    }

    note_date_obj = datetime.strptime(note_details.entry_date, "%Y-%m-%d")

    general_details["note_details"] = {
        "company_name": company.name,
        "date": cleanup_date_format(note_date_obj), 
        "subject": note_details.subject, 
        "note_text": note_details.note_text, 
    }

    return render_template("view_specific_company_note.html", general_details=general_details)