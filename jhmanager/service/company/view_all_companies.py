from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_company_fields


def display_all_companies_for_user(user_id, companyRepo, applicationsRepo):
    company_entries = companyRepo.getAllCompanyEntriesForUser(user_id)
    company_details = None 

    general_details = {
        "empty_table": False, 
        "message": None, 
        "add_company_url": '/address_book/add_company'
    }

    if not company_entries:
        general_details["empty_table"] = True
        general_details["message"] = "No contacts yet. Add your first application."

    else: 
        company_details = {}
        entry_id = 0
        for company in company_entries:
            entry_id += 1
            company_id = company.company_id
            company_details["fields"][entry_id] = {
                "company_id": company_id,
                "company_name": company_name,
                "view_company": '/company/{}/view_company'.format(company_id)
            }
            cleanup_company_fields(company_details)


    return render_template("view_company_directory.html", general_details=general_details, company_details=company_details)