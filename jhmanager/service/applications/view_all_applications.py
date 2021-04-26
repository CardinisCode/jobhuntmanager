from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_application_fields


def display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {
        "fields": {}, 
        "empty_table": True, 
        "links": {}
    }
    
    # Let's take the details from "top10applications" 
    # and restructure the data for our html page:
    if top_ten_applications != None:
        display_details["empty_table"] = False
        entry_id = 0
        for application in top_ten_applications:
            entry_id += 1
            app_id = application.app_id
            app_date = application.app_date
            company_id = application.company_id

            # # Now that we have the company_id, we can grab the company_name:
            company_name = companyRepo.getCompanyById(company_id).name

            display_details["fields"][app_id] = {
                "app_id": entry_id,
                "app_date": application.app_date,
                "company_name": company_name,
                "job_role": application.job_role,
                "interview_stage": application.interview_stage,                  
                "salary": application.salary,       
                "emp_type": application.employment_type,          
                "view_more": "/applications/{}".format(app_id),
            }
            display_details["app_count"] = entry_id
            cleanup_application_fields(display_details, app_id) 

    display_details["links"] = {
        "add_application": "/add_job_application", 
        "delete_all_applications": '/applications/delete_all_applications'
    }

    return render_template("applications.html", display_details=display_details)