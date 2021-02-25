from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["headings"] = {
        "headings_list" : ["ID#", "Date", "Company Name", "Job Role", "Employment Type",  "Interview Stage", "Contact Received", "Salary", "Platform / Job Board", "View More"]
    }
    display_details["fields"] = {}
    display_details["empty_table"] = True
    
    # Let's take the details from "top10applications" 
    # and restructure the data for our html page:

    if top_ten_applications != None:
        display_details["empty_table"] = False
        for application in top_ten_applications:
            app_id = application.app_id
            app_date = application.app_date
            emp_type = application.employment_type
            company_id = application.company_id
            salary = application.salary
            platform = application.platform
            interview_stage = application.interview_stage

            # # Now that we have the company_id, we can grab the company_name:
            company_name = companyRepo.getCompanyById(company_id).name

            # # Before adding Interview_stage to our display dict, let's format it's presentation:
            if interview_stage == 0:
                Interview_stage_str = "No Interview lined up yet."
            else:
                Interview_stage_str = "Interview #{interview_stage} lined up.".format(interview_stage=str(interview_stage))

            # # application_url = "/applications/{application_id}"
            application_url = "/applications/{app_id}"

            display_details["fields"][app_id] = {
                "app_id": {
                    "label": "ID#", 
                    "data": app_id,
                },
                
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
                    "data": application.job_role,
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
                    "data": application.contact_received.capitalize(),                  
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
                    "data": application_url,
                }
            }

            # Let's clean up the emp_type so its output is more presentable:
            if emp_type == "full_time":
                display_details["fields"][app_id]["emp_type"]["data"] = "Full Time"
            
            elif emp_type == "part_time":
                display_details["fields"][app_id]["emp_type"]["data"]= "Part Time"

            elif emp_type == "temporary":
                display_details["fields"][app_id]["emp_type"]["data"] = "Temp"

            elif emp_type == "contract":
                display_details["fields"][app_id]["emp_type"]["data"] = "Contract"

            elif emp_type == "other_emp_type": 
                display_details["fields"][app_id]["emp_type"]["data"] = "Other"

            else: 
                display_details["fields"][app_id]["emp_type"]["data"] = "Not Provided"

            # If these fields values are "N/A", lets rather display a blank field to user:
            if platform == "N/A":
                display_details["fields"][app_id]["platform"]["data"] = ""

            if salary == "N/A":
                display_details["fields"][app_id]["salary"]["data"] = ""



    return render_template("applications.html", display_details=display_details)