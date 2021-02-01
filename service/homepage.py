from flask import Flask, render_template, session
import datetime

def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo):
    current_date = datetime.date.today()
    applications_today = applicationsRepo.grabTodaysApplicationCount(current_date, user_id)
    top_5_applications = applicationsRepo.grabTop5ApplicationsFromHistory(user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(str(current_date), user_id)

    interviews_today_count = 0
    for interview in interviews_today:
        interviews_today_count += 1

    message = "All good!"

    if applications_today == None:
        message = "Not successful"

    render_info = {
        'current_date': current_date,
        "applications_today": applications_today,
        "interviews_today": interviews_today_count,
        "message": message,
        "top_5_applications": top_5_applications,
    }

    return render_template("index.html", render_info=render_info)