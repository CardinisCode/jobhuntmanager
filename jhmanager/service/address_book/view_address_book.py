from flask import Flask, render_template, session, request, redirect, flash


def display_address_book(user_id, companyRepo, contactRepo):
    display = {
        "company_directory": '/address_book/company_directory', 
        "add_company": '/address_book/add_company', 
        "empty_list": True
    }

    company_list = companyRepo.getTop6CompaniesByUserID(user_id)

    company_details = {}
    if company_list:
        display["empty_list"] = False
        company_details["fields"] = {}
        for company in company_list:
            company_id = company.company_id
            view_company = '/company/{}/view_company'.format(company_id)
            company_details["fields"][company_id] = {
                "name": company.name,
                "description": company.description,
                "industry": company.industry, 
                "view_company": view_company
            }

    contacts_list = contactRepo.getContactsByUserID(user_id)
    contacts_details = {
        "empty_list": True, 
        "message": "No contacts to display", 
        "view_contacts": '/address_book/contact_list',
        "add_new_contact": '/address_book/contact_list/add_contact'
    }
    if contacts_list:
        contacts_details["fields"] = {}
        contacts_details["empty_list"] = False
        contacts_details["message"] = "There are contacts to display"

    return render_template("view_address_book.html", display=display, company_details=company_details, contacts_details=contacts_details)


