from flask import Flask, render_template, session, request, redirect, flash


def delete_company_from_db(company_id, companyRepo, companyNotesRepo, applicationsRepo, interviewsRepo, interviewPrepRepo, userNotesRepo, jobOffersRepo):
    # When deleting a company, we're also deleting everything connected to that company ID:
    companyRepo.deleteByCompanyID(company_id)
    companyNotesRepo.deleteByCompanyID(company_id)
    jobOffersRepo.deleteByCompanyID(company_id)

    applications = applicationsRepo.getApplicationsByCompanyID(company_id)
    application_id = None
    if applications:
        for application in applications:
            application_id = application.app_id
            interviewsRepo.deleteByApplicationID(application_id)
            interviewPrepRepo.deleteByApplicationID(application_id)
            userNotesRepo.deleteByApplicationID(application_id)
    applicationsRepo.deleteByCompanyID(company_id)
    flash("All Applications, Notes, Interviews & Prep related to this company have been deleted.")

    return redirect("/address_book")
