from flask import Flask, render_template, session, request, redirect


def display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo):
    company_id = applicationsRepo.grabApplicationByID(application_id).company_id
    company_name = companyRepo.getCompanyById(company_id).name

    details = {
        "application_id": application_id,
        "company_name": company_name
    }

    return render_template('add_interview.html', add_interview_form=add_interview_form, details=details)