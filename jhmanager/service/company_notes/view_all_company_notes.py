from flask import Flask, render_template, session, request, redirect, flash


def display_all_notes_for_a_company(company_id, user_id, companyRepo, companyNotesRepo):
    company = companyRepo.getCompanyById(company_id)
    
    general_details = { 
        "add_note_url": '/company/{}/add_company_note'.format(company_id),
        "company_name": company.name,
        "empty_table": True, 
        "return_to_company_url": '/company/{}/view_company'.format(company_id), 
        "return_to_address_book": '/address_book'
    }
    fields = (company_id, user_id)
    notes_history = companyNotesRepo.getAllNotesByCompanyID(fields)
    note_details = None 

    if notes_history != None:
        general_details["empty_table"] = False 
        general_details["headings"] = ["ID#", "Date", "Subject", "Note", ""]
        entry_id = 0
        note_details = {}
        for note in notes_history: 
            entry_id += 1
            subject = note.subject
            company_note_id = note.company_note_id
            view_more_url = '/company/{}/company_note/{}/view_note_details'.format(company_id, company_note_id)
            update_note_url = '/company/{}/company_note/{}/update_note'.format(company_id, company_note_id)
            delete_note_url = '/company/{}/company_note/{}/delete_note'.format(company_id, company_note_id)
            note_text = note.note_text[0:10] + "..."
            note_details[entry_id] = {
                "Date": note.entry_date, 
                "Subject": note.subject.capitalize(), 
                "Note_Text": note_text, 
                "View_More": view_more_url,
                "Update_url": update_note_url,
                "Delete_url": delete_note_url
            }

    return render_template("view_company_notes.html", general_details=general_details, note_details=note_details)