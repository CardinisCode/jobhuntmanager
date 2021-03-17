from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["fields"] = {}
    display_details["empty_table"] = True
    
    # Let's take the details from "top10applications" 
    # and restructure the data for our html page:
    if top_ten_applications != None:
        display_details["empty_table"] = False
        display_details["headings"] = {
        "headings_list" : ["#", "Date", "Company Name", "Job Role", "Interview Stage", "Salary", "More..."]
        }
        
        entry_id = 0
        for application in top_ten_applications:
            entry_id += 1
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
            application_url = "/applications/{}".format(app_id)
            delete_url = "/applications/{}/delete".format(app_id)

            display_details["fields"][app_id] = {
                "app_id": {
                    "label": "#", 
                    "data": entry_id,
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
                "interview_stage": {
                    "label": "Interview Stage",
                    "data": Interview_stage_str,                  
                },
                "salary": {
                    "label": "Salary",
                    "data": salary,                 
                },
                "view_more": {
                    "label": "View More", 
                    "data": application_url,
                }, 
                "delete": {
                    "label": "Delete Note", 
                    "data": delete_url,
                }
            }

            if salary == "N/A":
                display_details["fields"][app_id]["salary"]["data"] = ""



    return render_template("applications.html", display_details=display_details)