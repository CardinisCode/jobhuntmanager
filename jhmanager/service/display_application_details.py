from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


# def display_application_details(session, user_id, applicationsRepo, application_id):
def display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo):
    results = applicationsRepo.grabApplicationDetailsByApplicationID(application_id)
    application_details = {}

    for row in results:
        company_id = row[2]
        company_name = companyRepo.grab_company_name(user_id, company_id)
        application_details["fields"] = {
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

    application_details["app_id"] = application_id
    # urls_details = {
    #     "delete_application": delete_application
    # }

    # Now I want to display all the interviews for this application_id:
    all_interviews_for_app_id = interviewsRepo.grabAllInterviewsForApplicationID(application_id)

    # Lets build the interview dict to be displayed to the user.
    # I'll set the default value for "fields" key to be None, as there are currently no values to display.
    interview_details = {
        "message": "No interviews added yet for this application.", 
        "headings": ["ID#", "Date", "Time", "Interview Type", "Status", "Location", "View More"], 
        "fields": None
    }
    
    interview_details["fields"] = {}
    # In the case that there are actually interviews for this application, 
    # we want to grab those details & update the "fields" value to contain these values.
    # These values will be displayed to the user, in a table format. 
    if all_interviews_for_app_id != None: 
        for interview in all_interviews_for_app_id:
            interview_id = str(interview[0])
            interview_details["fields"][interview_id] = {
                "ID#": interview_id, 
                "Date": interview[2], 
                "Time": interview[3],
                "Interview Type": interview[4], 
                "Status": interview[9],
                "Location": interview[5],
                "View More": ""
            }

            # interview_id = interview[0]
            # interview_date = interview[2]
            # interview_time = interview[3]
            # interview_type = interview[4]
            # location = interview[5]
            # medium = interview[6]
            # other_medium = interview[7]
            # contact_number = interview[8]
            # status = interview[9]
            # interviewers = interview[10]


    return render_template("view_application.html", details=application_details, interview_details=interview_details)
