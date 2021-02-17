from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["headings"] = {
        "headings_list" : ["ID#", "Date", "Company Name", "Job Role", "Employment Type", "Salary", "Platform / Job Board",  "Interview Stage", "Contact Received", "View More"]
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
        company_id = details_list[1]
        app_date = details_list[2]
        emp_type = details_list[4]
        salary = details_list[5]
        platform = details_list[6] 
        interview_stage = details_list[7]

        # Now that we have the company_id, we can grab the company_name:
        company_name = companyRepo.grab_company_name(user_id, company_id)

        # Before adding Interview_stage to our display dict, let's format it's presentation:
        if interview_stage == "N/A":
            Interview_stage_str = "No Interview lined up yet."
        else:
            Interview_stage_str = "Interview #{interview_stage} lined up.".format(interview_stage=str(interview_stage))

        display_details[app_id] = {
            "app_date":  {
                "label": "Date & Time",
                "data": app_date,
            },
            "company_name": {
                "label": "Company",
                "data": company_name,
            },
            "job_role": {
                "label": "Job Role",
                "data": details_list[3],
            },
            "emp_type": {
                "label": "Employment Type",
                "data": emp_type,
            },
            "interview_stage": {
                "label": "Interview Stage",
                "data": Interview_stage_str,                  
            },
            "contact_received": {
                "label": "Contact Received",
                "data": details_list[9].capitalize(),                  
            }, 
            "salary": {
                "label": "Salary",
                "data": salary,                 
            },
            "platform": {
                "label": "Platform / Job Board", 
                "data": platform,                
            },
            "view_more": {
                "label": "View More", 
                "data": "",
            }
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

        # If these fields values are "N/A", lets rather display a blank field to user:
        if platform == "N/A":
            display_details[app_id]["platform"]["data"] = ""

        if salary == "N/A":
            display_details[app_id]["salary"]["data"] = ""



    return render_template("applications.html", display_details=display_details)