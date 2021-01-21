from flask import Flask, render_template, session, request, redirect
import datetime


def display_all_applications_current_user(session, user_id, applicationsRepo):
    users_applications = applicationsRepo.grabApplicationHistory(user_id)
    display_details = {}

    for application in users_applications:
        app_id = application[0]

        company_name = application[1]
        app_date = application[2]
        job_role = application[3]
        platform = application[4]
        employment_type = application[8]

        display_details[app_id] = {
            "app_date": app_date,
            "company_name": company_name, 
            "job_role": job_role,
            "platform": platform, 
            "employment_type": employment_type
        }


        # # for item in application:
        # raise ValueError("Application ID:", display_details)

    return render_template("applications.html", display_details=display_details)