from flask import Flask, render_template, session, request, redirect
from jhmanager.forms.add_application_form import AddApplicationForm


def display_update_application_form(session, user_id, application_id, companyRepo, applicationsRepo):
    application_details = applicationsRepo.grabApplicationByID(application_id)
    company_id = application_details.company_id
    company_name = companyRepo.getCompanyById(company_id).name

    # Now to instantiate the AddApplicationForm using the details for this application:
    update_form = AddApplicationForm(obj=application_details)

    fields = {
        "Company Name": company_name,
        "application_id": application_id
    }

    return render_template("update_application.html", fields=fields, update_form=update_form)