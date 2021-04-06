from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format


def update_grid_size(display_details):
    grid_size = display_details["grid_size"]
    app_count = display_details["app_count"]
    if app_count == 1:
        display_details["grid_size"] = app_count
    elif app_count % 3 == 0: 
        display_details["grid_size"] = 3
    elif app_count % 2 == 0:
        display_details["grid_size"] = 2 
    else: 
        display_details["grid_size"] = 4



def cleanup_fields(display_details, app_id):
    interview_stage = display_details["fields"][app_id]["interview_stage"]
    app_date = display_details["fields"][app_id]["app_date"]
    salary = display_details["fields"][app_id]["salary"]

    if interview_stage == 0:
        Interview_stage_str = "No Interview lined up yet."
    else:
        Interview_stage_str = "Interview #{interview_stage} lined up.".format(interview_stage=str(interview_stage))

    display_details["fields"][app_id]["interview_stage"] = Interview_stage_str

    if salary == "N/A":
        display_details["fields"][app_id]["salary"] = None

    date_obj = datetime.strptime(app_date, "%Y-%m-%d")
    display_details["fields"][app_id]["app_date"] = cleanup_date_format(date_obj)




def display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["fields"] = {}
    display_details["empty_table"] = True
    display_details["grid_size"] = None
    
    # Let's take the details from "top10applications" 
    # and restructure the data for our html page:
    if top_ten_applications != None:
        display_details["empty_table"] = False
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

            # # application_url = "/applications/{application_id}"
            application_url = "/applications/{}".format(app_id)
            delete_url = "/applications/{}/delete".format(app_id)

            display_details["fields"][app_id] = {
                "app_id": entry_id,
                "app_date": app_date,
                "company_name": company_name,
                "job_role": application.job_role,
                "interview_stage": application.interview_stage,                  
                "salary": salary,                 
                "view_more": application_url,
            }
            display_details["app_count"] = entry_id
            cleanup_fields(display_details, app_id) 

        update_grid_size(display_details)

    return render_template("applications.html", display_details=display_details)