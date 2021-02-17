from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


# def display_application_details(session, user_id, applicationsRepo, application_id):
def display_application_details(session, user_id, applicationsRepo, application_id, companyRepo):
    results = applicationsRepo.grabApplicationDetailsByApplicationID(application_id)
    details = {}

    for row in results:
        company_id = row[2]
        company_name = companyRepo.grab_company_name(user_id, company_id)
        details = {
            "Date": row[3],
            "Time": row[4],
            "Company Name": company_name,
            "Job Role": row[5],
            "Platform": row[6],
            "Interview Stage": row[7],
            "Employment Type": row[8],
            "Contact Received?": row[9],
            "Location": row[10],
            "Job Description": row[11],
            "Job Perks": row[13], 
            "Company Description": row[14],
            "Tech Stack": row[15],
            "Job URL": row[16],
            "Job Ref": row[17],
            "Salary": row[18], 
            "User Notes": row[12]
        }

    return render_template("view_application.html", details=details)