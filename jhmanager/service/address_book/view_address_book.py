from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_contact_fields import cleanup_each_contact_entry


def display_address_book(user_id, companyRepo, contactRepo):
    company_list = companyRepo.getTop8CompaniesByUserID(user_id)
    company_contacts = {
        "empty_list": True,
        "fields": None
    }

    if company_list:
        company_contacts["empty_list"] = False
        company_contacts["fields"] = {}
        for company in company_list:
            company_id = company.company_id
            view_company = '/company/{}/view_company'.format(company_id)
            company_contacts["fields"][company_id] = {
                "name": company.name,
                "description": company.description,
                "industry": company.industry, 
                "location": company.location,
                "view_company": view_company
            }

    contacts_list = contactRepo.getTop8ContactsByUserID(user_id)
    indiv_contacts = {
        "empty_list": True, 
        "fields": None,
        "message": "No contacts to display", 
    }
    if contacts_list:
        indiv_contacts["fields"] = {}
        indiv_contacts["empty_list"] = False

        for contact in contacts_list:
            contact_id = contact.contact_id
            indiv_contacts["fields"][contact_id] = {
                "full_name": contact.full_name, 
                "job_title": contact.job_title,
                "company_name": contact.company_name, 
                "view_contact": '/address_book/contact_list/{}/view_contact'.format(contact_id)
            }
            cleanup_each_contact_entry(indiv_contacts, contact_id)

    general_details = {}
    general_details["links"] = {
        "company_directory": '/address_book/company_directory', 
        "add_company": '/address_book/add_company', 
        "view_contacts": '/address_book/contact_list',
        "add_new_contact": '/address_book/contact_list/add_contact'
    }

    return render_template("view_address_book.html", general_details=general_details, company_contacts=company_contacts, indiv_contacts=indiv_contacts)


