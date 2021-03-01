from flask import Flask, render_template, session, request, redirect


def display_user_notes_form(notes_form, application_id, companyRepo, applicationsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "application_id": application.app_id,
        "company_name": company.name
    }

    return render_template("add_notes.html", notes_form=notes_form, details=details)