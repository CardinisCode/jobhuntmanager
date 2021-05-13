from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def display_add_company_application_form(add_application_form, company_id, companyRepo):
    details = {
        "company_name": companyRepo.getCompanyById(company_id).name,
        "action_url": '/company/{}/add_job_application'.format(company_id)
    }

    return render_template('add_company_job_application.html', add_application_form=add_application_form, details=details)


def add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, application_form, company_id):
    # We need to grab current day's date & time when user adds a new application:
    application_datetime = datetime.now()

    # Now to grab the date value & convert it to string:
    app_date = application_datetime.date()
    date_format = "%Y-%m-%d"
    app_date_str = app_date.strftime(date_format)

    # Now to grab the time value & convert it to string:
    app_time = application_datetime.time()
    time_format = "%H:%M"
    app_time_str = app_time.strftime(time_format)

    # user_id, company_id, app_date, app_time, date_posted, job_role, platform, employment_type, job_description, user_notes, job_perks, tech_stack, job_url, job_ref, salary
    fields = {
        "user_id": user_id, 
        "company_id": company_id, 
        "app_date": app_date_str, 
        "app_time": app_time_str, 
        "date_posted": application_form.date_posted.data, 
        "job_role": application_form.job_role.data,
        "platform": application_form.platform.data, 
        "employment_type": application_form.emp_type.data,
        "job_description": application_form.job_description.data, 
        "user_notes": application_form.user_notes.data, 
        "job_perks": application_form.job_perks.data,
        "tech_stack": application_form.tech_stack.data, 
        "job_url": application_form.job_url.data,
        "job_ref": application_form.job_ref.data, 
        "salary": application_form.salary.data
    }

    # Before we put these values into the SQL table, let's first make sure the fields aren't blank:
    for heading, value in fields.items():
        if value == "":
            fields[heading] = "N/A"

    # Now we finish off by adding the details into the SQL db:
    application_id = applicationsRepo.createApplication(fields)

    return application_id


def post_add_company_job_application(user_id, company_id, applicationsRepo, companyRepo, add_job_app_form):

    # Lets add these fields to our function that will structure this data into a dict:
    application_id = add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, add_job_app_form, company_id)

    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)