from flask import Flask, render_template, session, request, redirect


def display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo):
    company_id = applicationsRepo.grabApplicationByID(application_id).company_id
    company_name = companyRepo.getCompanyById(company_id).name

    details = {
        "application_id": application_id, 
        "interview_id": interview_id, 
        "company_name": company_name
    }

    return render_template("update_interview.html", update_interview_form=update_interview_form, details=details)
