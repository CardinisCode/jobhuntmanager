from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def cleanup_interview_fields(interview_fields, interview_id):
    # Lets start by grabbing the fields we want from the dict:
    interview_type = interview_fields[interview_id]["Interview Type"]
    status = interview_fields[interview_id]["Status"]

    # Now I can optimise the presentation of the values for these variables:
    if interview_type == "video_or_online":
        interview_fields[interview_id]["Interview Type"] = "Video / Online"
    elif interview_type == "in_person":
        interview_fields[interview_id]["Interview Type"] = "In Person / On Site"
    else:
        interview_fields[interview_id]["Interview Type"] = "Phone Call"

    # Now to focus on 'status':
    if status == "upcoming":
        status = 'Upcoming Interview'

    elif status == "done":
        status = 'Interview Done'
    
    elif status == "cancelled":
        status = 'The interview has been cancelled'
    
    else:
        status = 'Interview has been post-poned'
    
    interview_fields[interview_id]["Status"] = status


def cleanup_application_details(application_details):
   
    for heading, value in application_details["fields"].items():
        if value == "N/A":
            application_details["fields"][heading] = None

    interview_stage = application_details["fields"]["interview_stage"]
    if interview_stage == 0:
        application_details["fields"]["interview_stage"] = "No interview lined up yet."

    emp_type = application_details["fields"]["Type"]
    if emp_type == "full_time":
        application_details["fields"]["Type"] = "Full Time"
    elif emp_type == "part_time":
        application_details["fields"]["Type"] = "Part Time"
    elif emp_type == "temp":
        application_details["fields"]["Type"] = "Temporary"
    elif emp_type == "other_emp_type": 
        application_details["fields"]["Type"] = "Other"
    else:
        application_details["fields"]["Type"] = emp_type.capitalize()
    

def display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    app_date = application.app_date
    app_time = application.app_time
    company_id = application.company_id
    company = companyRepo.getCompanyById(company_id)

    application_details = {}
    application_details["fields"] = {
        "Job Ref" : application.job_ref,
        "Date": app_date, 
        "Time": app_time, 
        "Job Role" : application.job_role, 
        "Description" : application.job_description,
        "Perks" : application.job_perks,
        "Technology Stack" : application.tech_stack,
        "Salary" : application.salary,
        "Platform": application.platform, 
        "interview_stage" : application.interview_stage,
        "Type" : application.employment_type, 
        "Contact Received?" : application.contact_received, 
        "Job Url" : application.job_url,
    }
    cleanup_application_details(application_details)

    application_details["app_id"] = application_id

    user_notes = application.user_notes
    if user_notes == "N/A": 
        application_details["user_notes"] = None
    else:
        application_details["user_notes"] = user_notes

    # Lets grab some company details:
    company_details = {}
    company_details["fields"] = {
        "Company ID": company.company_id,
        "Company Name": company.name, 
        "Description": company.description, 
        "Location": company.location,
        "Industry": company.industry, 
        "Interviewers": company.interviewers
    }

    # Now I want to display all the interviews for this application_id:
    all_interviews_for_app_id = interviewsRepo.grabAllInterviewsForApplicationID(application_id)

    # Lets build the interview dict to be displayed to the user.
    # I'll set the default value for "fields" key to be None, as there are currently no values to display.
    interview_details = {
        "message": "No interviews added yet for this application.", 
        "headings": ["ID#", "Date", "Time", "Interview Type", "Status", "Location", "View More"], 
        "app_id": application_id, 
        "empty_fields" : True,
    }
    
    # In the case that there are actually interviews for this application, 
    # we want to grab those details & update the "fields" value to contain these values.
    # These values will be displayed to the user, in a table format. 
    interview_fields = {}
    if all_interviews_for_app_id != None:
        interview_details["empty_fields"] = False 
        for interview in all_interviews_for_app_id:
            interview_id = str(interview[0])
            status = interview[9]
            view_more_url = "/applications/{application_id}"
            location = interview[5]
            interview_fields[interview_id] = {
                "ID#": interview_id, 
                "Date": interview[2], 
                "Time": interview[3],
                "Interview Type": interview[4], 
                "Status": status,
                "Location": location,
                "View More": view_more_url,
            }

            cleanup_interview_fields(interview_fields, interview_id)


    return render_template("view_application.html", details=application_details, interview_details=interview_details, interview_fields=interview_fields, company_details=company_details)
