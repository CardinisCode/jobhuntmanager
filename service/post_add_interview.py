from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def post_add_interview(session, user_id, form):
    details = {}

    details = {
        "company_name": form.company_name,
        "interview_date": form.interview_date, 
        "interview_time": form.interview_time,
        "job_role": form.job_role, 
        "interview_type": form.interview_type
    }

    if form.interviewer_names.data != "Unknown at present":
        details["interviewers"] = form.interviewer_names

    if form.interview_type.data == 'in_person':
        details["interview_location"] = form.interview_location

    if form.interview_type.data == 'video_or_online':
        details["video_medium"] = form.interview_medium

    if form.interview_type.data == 'video' and form.interview_medium.data == 'other':
        details["other_medium"] = form.other_medium

    if form.interview_type.data == 'phone_call': 
        details["phone_call"] = form.phone_call


    return render_template("interview_details.html", details=details)


