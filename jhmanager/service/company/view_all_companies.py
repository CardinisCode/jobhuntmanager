from jhmanager.repo.company import CompanyRepository
from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_company_fields


def display_all_companies_for_user(user_id, companyRepo, applicationsRepo):
    company_entries = companyRepo.getAllCompanyEntriesForUser(user_id)

    company_contacts = {
        "empty_list": True, 
        "fields": None,
        "message": "No contacts yet. Add your first application.", 
    }

    if company_entries:
        company_contacts["fields"] = {}
        company_contacts["empty_list"] = False 
        company_contacts["message"] = None
        entry_id = 0
        for company in company_entries:
            entry_id += 1
            company_id = company.company_id
            company_contacts["fields"][entry_id] = {
                "company_name": company.name,
                "view_company": '/company/{}/view_company'.format(company_id)
            }
            cleanup_company_fields(company_contacts, entry_id)

    general_details = {
        "add_company_url": '/address_book/add_company', 
        "company_contacts": company_contacts
    }

    return render_template("view_company_directory.html", general_details=general_details)