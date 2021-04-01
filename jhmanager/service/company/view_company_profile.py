from flask import Flask, render_template, session, request, redirect, flash


def cleanup_fields(company_details):
    contact_number = company_details["contact_number"]["data"]

    if contact_number == "Unknown at present":
        company_details["contact_number"]["data"] = None


def display_company_profile(company_id, applicationsRepo, companyRepo):
    company = companyRepo.getCompanyById(company_id)

    update_url = '/company/{}/update_company'.format(company_id)
    add_note_url = '/company/{}/add_company_note'.format(company_id)
    view_notes_url = '/company/{}/view_all_company_notes'.format(company_id)
    delete_url = '/company/{}/delete_company'.format(company_id)

    company_details = {
        "description": {
            "label": "Description: ", 
            "data": company.description
        }, 
        "location": {
            "label": "Location: ", 
            "data": company.location
        },
        "industry": {
            "label": "Industry: ", 
            "data": company.industry            
        },
        "interviewers": {
            "label": "Interviewers: ", 
            "data": company.interviewers            
        },
        "contact_number": {
            "label": "Contact Number: ", 
            "data": company.contact_number
        }
    }
    cleanup_fields(company_details)

    company_website = company.url
    if company_website == "N/A" or company_website == "http://" or company_website == "https://":
        company_website = None

    general_details = {
        "company_name": company.name, 
        "company_website": company_website,
        "update_url": update_url, 
        "add_note_url": add_note_url,
        "view_notes_url": view_notes_url, 
        "add_job_application_url": '/company/{}/add_job_application'.format(company_id), 
        "delete_url": delete_url
    }

    return render_template("view_company_profile.html", general_details=general_details, company_details=company_details)