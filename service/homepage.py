from flask import Flask, render_template, session
import datetime

def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo):
    current_date = datetime.date.today()
    applications_today = applicationsRepo.searchApplicationHistory(current_date, user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(current_date, user_id)
    message = "All good!"

    if applications_today == None:
        message = "Not successful"

    render_info = {
        'current_date': current_date,
        "applications_today": applications_today,
        "interviews_today": interviews_today,
        "message": message,
    }

    return render_template("index.html", render_info=render_info)