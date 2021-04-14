from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format


def cleanup_emp_type_field(emp_type):
    updated_emp_type = ""
    if emp_type == "full_time":
        updated_emp_type = "Full Time"
    elif emp_type == "part_time":
        updated_emp_type = "Part Time"
    elif emp_type == "temp":
        updated_emp_type = "Temporary"
    elif emp_type == "other_emp_type": 
        updated_emp_type = "Other"
    else:
        updated_emp_type = emp_type.capitalize()
    
    return updated_emp_type


def cleanup_interview_stage(interview_stage): 
    updated_interview_stage = ""
    if interview_stage == 0:
        updated_interview_stage = "No interview lined up yet."
    else:
        updated_interview_stage = "Interview #" + str(interview_stage) + "."
    
    return updated_interview_stage


def cleanup_urls(url):
    if url == "N/A" or url == "n/a":
        return None

    elif url == "http://" or url == "https://":
        return None

    return url


def cleanup_details_for_specific_application(application_details):
    for heading, value in application_details["fields"].items():
        if value == "N/A":
            application_details["fields"][heading] = None

    interview_stage = application_details["fields"]["interview_stage"]
    application_details["fields"]["interview_stage"] = cleanup_interview_stage(interview_stage)

    time_posted = application_details["fields"]["time"]
    if time_posted:
        time_obj = datetime.strptime(time_posted, '%H:%M')
        application_details["fields"]["time"] = cleanup_time_format(time_obj)

    date_posted = application_details["fields"]["date"]
    if date_posted: 
        date_obj = datetime.strptime(date_posted, "%Y-%m-%d")
        application_details["fields"]["date"] = cleanup_date_format(date_obj)

    emp_type = application_details["fields"]["emp_type"]
    application_details["fields"]["emp_type"] = cleanup_emp_type_field(emp_type)

    description = application_details["fields"]["job_description"]
    if not description:
        application_details["fields"]["job_description"] = "None provided."


def cleanup_applications_for_dashboard(todays_applications, application_id):
    company_name = todays_applications["fields"][application_id]["company_name"]
    job_role = todays_applications["fields"][application_id]["job_role"]
    presentation_str = ""
    emp_type = cleanup_emp_type_field(todays_applications["fields"][application_id]["emp_type"])
    salary = todays_applications["fields"][application_id]["salary"]

    company_name_list = company_name.split(" ")
    updated_company_name = ""
    for name in company_name_list:
        updated_company_name += name.capitalize() + " "
    updated_company_name = updated_company_name.rstrip(" ")

    presentation_str += job_role + ", " + updated_company_name + ", " + emp_type
    
    if salary != "N/A":
        presentation_str += ", " + salary + "."

    todays_applications["fields"][application_id]["salary"] = salary
    todays_applications["fields"][application_id]["presentation_str"] = presentation_str
    todays_applications["fields"][application_id]["emp_type"] = emp_type


def cleanup_application_fields(display_details, app_id):
    interview_stage = display_details["fields"][app_id]["interview_stage"]
    app_date = display_details["fields"][app_id]["app_date"]
    salary = display_details["fields"][app_id]["salary"]

    if interview_stage == 0:
        Interview_stage_str = "No Interview lined up yet."
    else:
        Interview_stage_str = "Interview #{interview_stage}".format(interview_stage=str(interview_stage))

    display_details["fields"][app_id]["interview_stage"] = Interview_stage_str

    if salary == "N/A":
        display_details["fields"][app_id]["salary"] = None

    date_obj = datetime.strptime(app_date, "%Y-%m-%d")
    display_details["fields"][app_id]["app_date"] = cleanup_date_format(date_obj)
