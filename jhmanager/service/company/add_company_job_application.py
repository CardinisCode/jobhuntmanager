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

    # Before we add the fields to our SQL db, lets make sure we first grab the data for each field:
    job_role = application_form.job_role.data
    date_posted_data = application_form.date_posted.data

    # Since these are optional fields for the user, 
    # lets make sure each field actually has data to insert into the db:
    emp_type = application_form.emp_type.data
    if not emp_type:
        emp_type = "N/A"

    job_ref = application_form.job_ref.data
    if not job_ref:
        job_ref = "N/A"

    job_spec = application_form.job_description.data
    if not job_spec:
        job_spec = "N/A"

    perks = application_form.job_perks.data
    if not perks:
        perks = "N/A"    

    tech_stack = application_form.tech_stack.data
    if not tech_stack:
        tech_stack = "N/A" 

    salary = application_form.salary.data
    if not salary:
        salary = "N/A" 

    user_notes = application_form.user_notes.data
    if not user_notes:
        user_notes = "N/A" 

    platform = application_form.platform.data
    if not platform:
        platform = "N/A"     

    job_url = application_form.job_url.data
    if not job_url:
        job_url = "N/A" 

    location = companyRepo.getCompanyById(company_id).location

    # Now we finish off by adding the details into the SQL db:
    fields = (job_role, app_date_str, app_time_str, date_posted_data, emp_type, job_ref, job_spec, tech_stack, perks, platform, location, salary, user_notes, job_url, user_id, company_id)
    application_id = applicationsRepo.addApplicationToHistory(fields)

    return application_id


def post_add_company_job_application(user_id, company_id, applicationsRepo, companyRepo, add_job_app_form):

    # Lets add these fields to our function that will structure this data into a dict:
    application_id = add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, add_job_app_form, company_id)

    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)