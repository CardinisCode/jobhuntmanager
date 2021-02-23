from flask import Flask, render_template, session, request, redirect


def display_update_application_form(session, user_id, application_id, add_application_form, companyRepo, applicationsRepo):
    application_details = applicationsRepo.grabApplicationByID(application_id)
    company_id = application_details.company_id
    company_name = companyRepo.getCompanyById(company_id)
    raise ValueError("The application for Company:", company_name)

    display = {}

    return render_template("update_application.html", display=display)