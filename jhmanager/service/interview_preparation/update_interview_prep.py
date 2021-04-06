from flask import Flask, render_template, session, request, redirect, flash


def display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "company_name": company, 
        "action_url": '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
    }

    return render_template("update_interview_prep.html", details=details, update_interview_prep_form=update_interview_prep_form)