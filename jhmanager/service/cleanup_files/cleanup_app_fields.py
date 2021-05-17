from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_field_value


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


def cleanup_specific_job_application(application):
    for heading, value in application["fields"].items():
        if value == "N/A":
            application["fields"][heading] = None
        elif heading == "interview_stage":
            application["fields"][heading] = cleanup_interview_stage(value)
        elif heading == "emp_type":
            application["fields"][heading] = cleanup_emp_type_field(value)
        elif heading == "time":
            time_obj = datetime.strptime(value, '%H:%M')
            application["fields"][heading] = cleanup_time_format(time_obj)
        elif heading == "date":
            date_obj = datetime.strptime(value, "%Y-%m-%d")
            application["fields"][heading] = cleanup_date_format(date_obj)
        
        else:
            application["fields"][heading] = cleanup_field_value(value)


def cleanup_application_fields(application_details, app_id):
    for heading, value in application_details["fields"].items():
        if value == "N/A":
            application_details["fields"][heading] = None

    interview_stage = cleanup_interview_stage(application_details["fields"][app_id]["interview_stage"])
    application_details["fields"][app_id]["interview_stage"] = interview_stage

    emp_type = application_details["fields"][app_id]["emp_type"]
    application_details["fields"][app_id]["emp_type"] = cleanup_emp_type_field(emp_type)

    app_date = application_details["fields"][app_id]["app_date"]
    date_obj = datetime.strptime(app_date, "%Y-%m-%d")
    application_details["fields"][app_id]["app_date"] = cleanup_date_format(date_obj)
