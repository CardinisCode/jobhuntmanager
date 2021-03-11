from flask import Flask, render_template, session, request, redirect, flash


def display_company_profile(company_id, applicationsRepo, companyRepo):
    company = companyRepo.getCompanyById(company_id)

    general_details = {
        "company_name": company.name
    }

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
        "url": {
            "label": "Website: ", 
            "data": company.url             
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

    return render_template("view_company_profile.html", general_details=general_details, company_details=company_details)