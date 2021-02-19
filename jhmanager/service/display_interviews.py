from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo):
    application_details = applicationsRepo.grabApplicationDetailsByApplicationID(application_id)

    for application in application_details:
        company_id = application[2]

    company_name = companyRepo.getCompanyById(company_id).name




    return render_template("view_interview_details.html")
