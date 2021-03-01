from flask import Flask, render_template, session, request, redirect


def display_update_company_details_form(update_form, company, application):
    application_id = application.app_id

    details = {
        "company_name": company.name, 
        "application_id": application_id
    }
    
    return render_template("update_company.html", update_form=update_form, details=details)
