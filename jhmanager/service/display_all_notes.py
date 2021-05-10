from flask import Flask, render_template, session, request, redirect
from datetime import datetime, date
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_general_fields import get_count
from jhmanager.service.cleanup_files.cleanup_app_note_fields import cleanup_app_notes


def display_all_user_notes(user_id, appNotesRepo, companyRepo, applicationsRepo, companyNotesRepo):
    application_notes = appNotesRepo.getAppNotesByUserId(user_id)
    company_notes = companyNotesRepo.getCompanyNotesByUserID(user_id)
    all_applications = applicationsRepo.getAllApplicationsByUserID(user_id)
    application_count = get_count(all_applications)
    app_note_count = get_count(application_notes)

    all_companies = companyRepo.getAllCompanyEntriesForUser(user_id)
    company_count = get_count(all_companies)

    general_details = {
        "links": {}, 
        "app_notes_details": {}, 
        "company_notes_details": {},
        "application_count": application_count, 
        "app_note_count": app_note_count,  
        "company_count": company_count, 
        "display_bottom_links": True 
    }

    if company_count == 0 and application_count == 0:
        general_details["display_bottom_links"] = False 

    general_details["links"] = {
        "view_applications_url": '/applications',
        "view_companies_url": '/address_book', 
        "add_job_application": "/add_job_application", 
        "add_company": '/address_book/add_company'   
    }

    general_details["app_notes_details"] = {
        "empty_table": True, 
        "fields": None
    }

    general_details["company_notes_details"] = {
        "empty_table": True, 
        "fields": None
    }

    entry_id = 0
    if application_notes:
        general_details["app_notes_details"]["fields"] = {}
        for app_note in application_notes:
            entry_id += 1
            general_details["app_notes_details"]["empty_table"] = False
            app_notes_id = app_note.app_notes_id

            company = companyRepo.getCompanyById(app_note.company_id)
            application = applicationsRepo.grabApplicationByID(app_note.application_id)
            entry_date_obj =  datetime.strptime(app_note.entry_date, "%Y-%m-%d")
            
            # In case a note exists for an application that's already been deleted:
            if not application:
                appNotesRepo.deleteByAppNoteID(app_notes_id)
                continue

            view_note = '/applications/{}/app_notes/{}/view_note'.format(application.app_id, app_notes_id)

            general_details["app_notes_details"]["fields"][entry_id] = {
                "app_notes_id": app_note.app_notes_id, 
                "entry_date" : cleanup_date_format(entry_date_obj),
                "company_name": company.name, 
                "job_role": application.job_role,
                "description": app_note.description, 
                "view_note_url": view_note,
            }

    entry_note_count = 0
    if company_notes:
        general_details["company_notes_details"]["fields"] = {}
        general_details["company_notes_details"]["empty_table"] = False
        for company_note in company_notes: 
            entry_note_count += 1
            company_note_id = company_note.company_note_id
            company = companyRepo.getCompanyById(company_note.company_id)
            entry_date_obj = datetime.strptime(company_note.entry_date, "%Y-%m-%d")
            view_note_url = '/company/{}/company_note/{}/view_note_details'.format(company.company_id, company_note_id)
            general_details["company_notes_details"]["fields"][entry_note_count] = {
                "company_name": company.name, 
                "note_id": company_note.company_note_id,
                "entry_date": cleanup_date_format(entry_date_obj), 
                "subject": company_note.subject, 
                "view_company_note_url": view_note_url, 
            }

    return render_template("view_all_user_notes.html", general_details=general_details)