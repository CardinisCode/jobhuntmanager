from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time



def display_all_applications_current_user(session, user_id, applicationsRepo):
    top_ten_applications = applicationsRepo.grabTop10ApplicationsFromHistory(user_id)

    display_details = {}
    display_details["headings"] = {
        "headings_list" : ["ID#", "Date", "Company Name", "Job Role", "Employment Type", "Salary", "Stage", "Contact Received", "Job Ref", "Platform / Job Board"]
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

        display_details[app_id] = {
            "app_date":  {
                "label": "Application Date",
                "data": details_list[1],
            },
            "company_name": {
                "label": "Company",
                "data": details_list[3],
            },
            "job_role": {
                "label": "Job Role",
                "data": details_list[4],
            },
            "emp_type": {
                "label": "Employment Type",
                "data": details_list[6],                
            },
            "salary": {
                "label": "Salary",
                "data": details_list[9],                 
            },
            "interview_stage": {
                "label": "Interview Stage",
                "data": details_list[7],                  
            },
            "contact_received": {
                "label": "Contact Received",
                "data": details_list[8],                  
            }, 
            "job_ref": {
                "label": "Job Ref", 
                "data": details_list[2],
            },
            "platform": {
                "label": "Platform / Job Board", 
                "data": details_list[5],                
            }
        }

    # format = '%m/%d/%Y %H:%M:%S.%f'
    #     updated_date =  app_date.strftime("%Y %M %d %H:%M:%S%p")
    #     # raise ValueError("Date:", updated_date)
    #     # updated_date = datetime(*(time.strptime(app_date, format)[0:5]))


    return render_template("applications.html", display_details=display_details)