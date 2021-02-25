from flask import Flask, render_template, session, request, redirect


def display_interview_prep(interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo):
    details = {
        "application_id": application_id,
        "interview_id": interview_id,
    }

    return render_template("interview_prep.html", interview_prep_form=interview_prep_form, details=details)