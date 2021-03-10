from flask import Flask, render_template, session, request, redirect, flash


def display_all_companies_for_user(user_id, companyRepo, applicationsRepo):
    company_entries = companyRepo.getAllCompanyEntriesForUser(user_id)
    general_details = {}
    general_details["empty_table"] = False
    company_details = None 

    if not company_entries:
        general_details["empty_table"] = True

    else: 
        company_details = {}
        for company in company_entries:
            company_name = company.name
            company_id = company.company_id
            company_details[company_id] = {
                "company_name": company_name,
                "view_more_url": "View more..."
            }


    return render_template("view_address_book.html", general_details=general_details, company_details=company_details)