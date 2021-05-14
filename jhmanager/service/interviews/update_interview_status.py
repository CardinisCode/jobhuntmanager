from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type


def display_update_status_form(update_status_form, application_id, interview_id, interviewsRepo, applicationsRepo, companyRepo):
    interview = interviewsRepo.getInterviewByID(interview_id)
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    current_status = interview.status

    general_details = {
        "interview_details": {},
        "links": {}, 
        "company_name": company.name
    }

    general_details["links"] = {
        "action_url": '/applications/{}/interview/{}/update_interview_status'.format(application_id, interview_id),
        "view_interview": '/applications/{}/interview/{}'.format(application_id, interview_id),
        "view_application": '/applications/{}'.format(application_id)
    }

    return render_template("update_interview_status.html", update_status_form=update_status_form, general_details=general_details)


def post_update_interview_status(update_status_form, application_id, interview_id, interviewsRepo):
    fields = {
        "status": update_status_form.status.data, 
        "interview_id": interview_id
    }
    interviewsRepo.updateInterviewStatusByID(fields)

    flash("Interview Status has been updated!")
    redirect_url = '/applications/{}/interview/{}'.format(application_id, interview_id)

    return redirect(redirect_url)