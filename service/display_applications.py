from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time



def display_all_applications_current_user(session, user_id, applicationsRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["headings"] = {
        "headings_list" : ["ID#", "Date", "Company Name", "Job Role", "Employment Type", "Salary", "Platform / Job Board",  "Stage",  "Job Ref", "Contact Received"]
    }

    # Let's take the details from "applictop_ten_applicationsations" 
    # and restructure the data for our html page:
    for application in top_ten_applications:
        details_list = []
        for fields in application:
            details_list.append(fields)

        # Now that we have grabbed the fields for this current application
        # lets store these values in a dictionary to be displayed on the html page:
        app_id = details_list[0]
        emp_type = details_list[4]
        app_date = details_list[1]
        # raise ValueError(details_list)

        display_details[app_id] = {
            "app_date":  {
                "label": "Date & Time",
                "data": app_date,
            },
            "company_name": {
                "label": "Company",
                "data": details_list[2],
            },
            "job_role": {
                "label": "Job Role",
                "data": details_list[3],
            },
            "emp_type": {
                "label": "Employment Type",
                "data": emp_type,
            },
            "salary": {
                "label": "Salary",
                "data": details_list[5],                 
            },
            "platform": {
                "label": "Platform / Job Board", 
                "data": details_list[6],                
            },
            "interview_stage": {
                "label": "Interview Stage",
                "data": details_list[7],                  
            },
            "job_ref": {
                "label": "Job Ref", 
                "data": details_list[8],
            },
            "contact_received": {
                "label": "Contact Received",
                "data": details_list[9],                  
            }, 
        }

        # Let's clean up the emp_type so its output is more presentable:
        if emp_type == "full_time":
            display_details[app_id]["emp_type"]["data"] = "Full Time"
        
        elif emp_type == "part_time":
            display_details[app_id]["emp_type"]["data"]= "Part Time"

        elif emp_type == "temporary":
            display_details[app_id]["emp_type"]["data"] = "Temp"

        elif emp_type == "contract":
            display_details[app_id]["emp_type"]["data"] = "Contract"

        elif emp_type == "other_emp_type": 
            display_details[app_id]["emp_type"]["data"] = "Other"

        else: 
            display_details[app_id]["emp_type"]["data"] = "Not Provided"


        # Let's modify the app_date value so that it doesn't include the Min's & Seconds:
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        updated_date_dateformat = datetime.strptime(app_date, date_format)
        updated_date = updated_date_dateformat.strftime("%m-%d-%Y %H:%M")
        
        # Now to update the app_date value in our display_details dictionary:
        display_details[app_id]["app_date"]["data"] = updated_date


    return render_template("applications.html", display_details=display_details)