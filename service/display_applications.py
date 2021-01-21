from flask import Flask, render_template, session, request, redirect
import datetime


def display_all_applications_current_user(session, user_id, applicationsRepo):
    users_applications = applicationsRepo.grabApplicationHistory(user_id)
    display_details = {
        "users_applications": users_applications
    }
    
    # running_count = 0

    # for application in users_applications:
    #     running_count += 1

    # for application in users_applications:
    #     raise ValueError(application)

    # for i in range(len(users_applications), -1, -1):
        # app_id = application[0]

        # company_name = application[1]
        # app_date = application[2]
        # job_role = application[3]
        # platform = application[4]
        # employment_type = application[8]

        # display_details[app_id] = {
        #     "app_date": app_date,
        #     "company_name": company_name, 
        #     "job_role": job_role,
        #     "platform": platform, 
        #     "employment_type": employment_type
        # }

    # display_details["user_id"] = user_id

        # for item in application:
        # raise ValueError(running_count)

    return render_template("applications.html", display_details=display_details)