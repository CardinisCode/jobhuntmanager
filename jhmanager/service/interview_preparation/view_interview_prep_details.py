from flask import Flask, render_template, session, request, redirect, flash


def display_interview_prep_details(application_id, interview_id, interview_prep_id, interviewPrepRepo, applicationsRepo, companyRepo):
    interview_prep = interviewPrepRepo.getEntryByInterviewPrepID(interview_prep_id)
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    general_details = {}
    interview_prep_details = {}

    return render_template("view_interview_prep_details.html", general_details=general_details, interview_prep_details=interview_prep_details)