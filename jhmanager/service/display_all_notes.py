from flask import Flask, render_template, session, request, redirect


def display_all_user_notes(user_id, appNotesRepo, companyRepo, applicationsRepo, companyNotesRepo):
    application_notes = appNotesRepo.getAppNotesByUserId(user_id)
    company_notes = companyNotesRepo.getCompanyNotesByUserID(user_id)

    app_notes_details = {
        "empty_table": True, 
        "view_applications_url": '/applications', 
        "fields": None
    }

    company_notes_details = {
        "empty_table": True, 
        "view_companies_url": '/address_book', 
        "fields": None
    }

    entry_id = 0
    if application_notes != None:
        for app_note in application_notes:
            entry_id += 1
            app_notes_details["fields"] = {}
            app_notes_details["empty_table"] = False
            app_notes_id = app_note.app_notes_id
            app_id = app_note.application_id
            company_id = app_note.company_id
            job_role = applicationsRepo.grabApplicationByID(app_id).job_role
            view_note = '/applications/{}/app_notes/{}/view_note'.format(app_id, app_notes_id)
            update_note = '/applications/{}/app_notes/{}/update_note'.format(app_id, app_notes_id)
            delete_note = '/applications/{}/app_notes/{}/delete_note'.format(app_id, app_notes_id)

            app_notes_details["fields"][entry_id] = {
                "app_notes_id": app_note.app_notes_id, 
                "entry_date" : app_note.entry_date,
                "company_name": companyRepo.getCompanyById(company_id).name, 
                "job_role": applicationsRepo.grabApplicationByID(app_id).job_role,
                "description": app_note.description, 
                "view_note_url": view_note,
                "update_note_url": update_note, 
                "delete_note_url": delete_note
            }
            app_notes_details["headings"] = ["#", "Entry Date", "Company Name", "Job Role", "Subject"]









    return render_template("view_all_user_notes.html", app_notes_details=app_notes_details, company_notes_details=company_notes_details)