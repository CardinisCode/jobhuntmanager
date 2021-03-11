from flask import Flask, render_template, session, request, redirect, flash


def display_all_company_notes(company_id, user_id, companyRepo, companyNotesRepo):
    company = companyRepo.getCompanyById(company_id)
    
    general_details = { 
        "add_note_url": '/company/{}/add_company_note'.format(company_id),
        "company_name": company.name,
        "empty_table": True
    }
    fields = (company_id, user_id)
    notes_history = companyNotesRepo.getAllNotesByCompanyID(fields)

    if notes_history != None:
        general_details["empty_table"] = False 
        entry_id = 0

        for note in notes_history: 
            entry_date = note.entry_date
            subject = note.subject
            note_text = note.note_text




    return render_template("view_company_notes.html", general_details=general_details)