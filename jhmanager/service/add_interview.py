from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def validateCompanyNameNotEmpty(company_name):
    emptyField = False

    if not company_name:
        company_name = True
        # flash("Please provide the name of the Company you're interviewing for/with.")

    return emptyField


def validateInterviewDateNotEmpty(interview_date):
    emptyField = False

    if not interview_date:
        emptyField = True
        flash("No date chosen. Please add a date for the interview.")

    return emptyField


def validateInterviewTimeNotEmpty(interview_time):
    emptyField = False

    if not interview_time:
        emptyField = True
        flash("No time selected / added. Please add a time for the interview.")

    return emptyField


def grabDetailsFromNewInterviewAndAddToRepo(session, user_id, interviewsRepo):
    company_name = request.form.get("company_name")
    emptyCompanyNameField = validateCompanyNameNotEmpty(company_name)
    if emptyCompanyNameField:
        flash("Please provide the name of the Company you're interviewing for/with.")
        # return redirect("/add_interview")

    interview_date = request.form.get("date")
    emptyDateField = validateInterviewDateNotEmpty(interview_date)
    if emptyDateField:
        return redirect("/add_interview")

    interview_time = request.form.get("time")
    emptyTimeField = validateInterviewTimeNotEmpty(interview_time)
    if emptyTimeField:
        return redirect("/add_interview")


    job_role = request.form.get("job_role")
    interviewers = request.form.get("interviewers")
    interview_type = request.form.get("interview_type")
    location = request.form.get("interview_location")
    interview_medium = request.form.get("video_interview_medium")
    other_medium = request.form.get("other_video_medium")

    if not company_name:
        company_name = "N/A"

    if not interview_date:
        interview_date = "N/A"

    if not interview_time:
        interview_time = "N/A"

    if not job_role:
        job_role = "N/A"


    return render_template("interviews.html")