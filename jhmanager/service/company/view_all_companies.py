from flask import Flask, render_template, session, request, redirect, flash


def display_all_companies_for_user(user_id, companyRepo, applicationsRepo):
    company_entries = companyRepo.getAllCompanyEntriesForUser(user_id)
    general_details = {}
    general_details["empty_table"] = False
    general_details["message"] = None
    company_details = None 

    if not company_entries:
        general_details["empty_table"] = True
        general_details["message"] = "No contacts yet. Add your first application."

    else: 
        company_details = {}
        entry_id = 0
        for company in company_entries:
            entry_id += 1
            company_name = company.name
            company_id = company.company_id
            view_more_url = '/company/{}/view_company'.format(company_id)
            name = "".join(company_name.split(" "))
            company_details[entry_id] = {
                "company_id": company_id,
                "company_name": company_name,
                "name": name,
                "view_more_url": view_more_url
            }


    return render_template("view_address_book.html", general_details=general_details, company_details=company_details)