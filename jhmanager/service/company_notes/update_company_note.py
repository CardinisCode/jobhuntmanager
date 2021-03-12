from flask import Flask, render_template, session, request, redirect, flash


def display_update_company_note_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo):
    company = companyRepo.getCompanyById(company_id)
    note_details = companyNotesRepo.getCompanyNoteByID(company_note_id)
    details = {
        "company_name": company.name,
        "action_url": '/company/{}/company_note/{}/update_note'.format(company_id, company_note_id),
    }

    return render_template("update_company_note.html", details=details, update_note_form=update_note_form)