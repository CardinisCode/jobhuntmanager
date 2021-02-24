from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def cleanup_interview_fields(interview_details, interview_id):
    # Lets start by grabbing the fields we want from the dict:
    interview_type = interview_details["fields"][interview_id]["Interview Type"]
    status = interview_details["fields"][interview_id]["Status"]

    # Now I can optimise the presentation of the values for these variables:
    if interview_type == "video_or_online":
        interview_details["fields"][interview_id]["Interview Type"] = "Video / Online"
    elif interview_type == "in_person":
        interview_details["fields"][interview_id]["Interview Type"] = "In Person / On Site"
    else:
        interview_details["fields"][interview_id]["Interview Type"] = "Phone Call"

    # Now to focus on 'status':
    if status == "upcoming":
        status = 'Upcoming Interview'

    elif status == "done":
        status = 'Interview Done'
    
    elif status == "cancelled":
        status = 'The interview has been cancelled'
    
    else:
        status = 'Interview has been post-poned'
    
    interview_details["fields"][interview_id]["Status"] = status


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

    # Now I want to display all the interviews for this application_id:
    all_interviews_for_app_id = interviewsRepo.grabAllInterviewsForApplicationID(application_id)

    # Lets build the interview dict to be displayed to the user.
    # I'll set the default value for "fields" key to be None, as there are currently no values to display.
    interview_details = {
        "message": "No interviews added yet for this application.", 
        "headings": ["ID#", "Date", "Time", "Interview Type", "Status", "Location", "View More"], 
        "fields": None, 
        "app_id": application_id
    }
    
    
    # In the case that there are actually interviews for this application, 
    # we want to grab those details & update the "fields" value to contain these values.
    # These values will be displayed to the user, in a table format. 
    
    if all_interviews_for_app_id != None:
        raise ValueError("SQL returned more than 1 value")
        interview_details["fields"] = {}
        for interview in all_interviews_for_app_id:
            interview_id = str(interview[0])
            status = interview[9]
            view_more_url = "/applications/{application_id}"
            location = interview[5]
            interview_details["fields"][interview_id] = {
                "ID#": interview_id, 
                "Date": interview[2], 
                "Time": interview[3],
                "Interview Type": interview[4], 
                "Status": status,
                "Location": location,
                "View More": view_more_url,
            }

            cleanup_interview_fields(interview_details, interview_id)


    return render_template("view_application.html", details=application_details, interview_details=interview_details)
