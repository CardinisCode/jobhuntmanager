from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_all_applications_current_user(session, user_id, applicationsRepo):
    users_applications = applicationsRepo.grabApplicationHistory(user_id)

    # format = '%m/%d/%Y %H:%M:%S.%f'

    # for application in users_applications:
    #     app_date = application[0]
    #     raise ValueError("Date type:", type(app_date))
    #     company_name = application[1]
    #     job_role = application[2]
    #     platform = application[3]
    #     employment_type = application[4]
    #     interview_stage = application[5]
    #     contact_received = application[6]


    #     updated_date =  app_date.strftime("%Y %M %d %H:%M:%S%p")
    #     # raise ValueError("Date:", updated_date)
    #     # updated_date = datetime(*(time.strptime(app_date, format)[0:5]))
    #     # raise ValueError(updated_date)

    # for application in users_applications:
    #     application[0] = "test"

    display_details = {
        "users_applications": users_applications,
    }

    return render_template("applications.html", display_details=display_details)