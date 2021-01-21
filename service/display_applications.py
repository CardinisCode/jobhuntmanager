from flask import Flask, render_template, session, request, redirect
from datetime import datetime


def display_all_applications_current_user(session, user_id, applicationsRepo):
    users_applications = applicationsRepo.grabApplicationHistory(user_id)

    # for application in users_applications:
    #     application[0] = "test"

    display_details = {
        "users_applications": users_applications,
    }

    return render_template("applications.html", display_details=display_details)