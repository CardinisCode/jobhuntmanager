from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_company_profile
from jhmanager.service.cleanup_files.cleanup_company_fields import cleanup_company_website


def display_company_profile(company_id, applicationsRepo, companyRepo):
    company = companyRepo.getCompanyById(company_id)

    company_details = {
        "company_name": company.name,
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
        }, 
        "all_fields_empty": False,
    }
    cleanup_company_profile(company_details)

    general_details = {
        "links": {}, 
        "company_details": company_details
    }

    general_details["links"] = {
        "company_website": cleanup_company_website(company.url),
        "update_company": '/company/{}/update_company'.format(company_id), 
        "add_note": '/company/{}/add_company_note'.format(company_id),
        "view_notes": '/company/{}/view_all_company_notes'.format(company_id), 
        "add_job_application": '/company/{}/add_job_application'.format(company_id), 
        "delete_company": '/company/{}/delete_company'.format(company_id)
    }

    return render_template("view_company_profile.html", general_details=general_details)