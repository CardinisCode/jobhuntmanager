from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def display_add_application_form(add_application_form):
    return render_template('add_job_application.html', add_application_form=add_application_form)


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

    date_posted = application_form.date_posted.data
    date_posted_str = date_posted.strftime(date_format)

    # Before we add the fields to our SQL db, lets make sure we first grab the data for each field:
    fields = {
        "user_id": user_id, 
        "company_id": company_id, 
        "app_date": app_date_str, 
        "app_time": app_time_str, 
        "date_posted": date_posted_str, 
        "job_role": application_form.job_role.data, 
        "platform": application_form.platform.data, 
        "employment_type": application_form.emp_type.data, 
        "job_description": application_form.job_description.data, 
        "user_notes": application_form.user_notes.data, 
        "job_perks": application_form.job_perks.data,
        "tech_stack": application_form.tech_stack.data, 
        "job_url": application_form.job_url.data, 
        "job_ref": application_form.job_ref.data, 
        "salary": application_form.salary.data,
    }

    # Now that we have the values stored, let's replaced empty fields with 'N/A':
    for heading, value in fields.items():
        if value == "": 
            fields[heading] = "N/A"
        elif value == "https://" or value == "http://":
            fields[heading] = "N/A"

    # Now we finish off by adding the details into the SQL db:
    application_id = applicationsRepo.addApplicationToHistory(fields)

    return application_id


def add_or_update_company(user_id, application_form, companyRepo, applicationsRepo):
    #Grab fields from form:

    company_name = application_form.company_name.data

    fields = {
        "name": company_name,
        "description": application_form.company_description.data, 
        "location" : application_form.location.data, 
        "industry" : application_form.industry.data, 
        "user_id" : user_id, 
    }

    existing_company = companyRepo.grabCompanyByNameAndUserID(company_name, user_id)

    if not existing_company:
        # Add the details into the company table for this user and return the company_id:
        company_id = companyRepo.create(fields)

    else:
        # Grab the existing company_id and update the details in the 'company' table for this company and user_id:
        company_id = existing_company.company_id
        fields['company_id'] = company_id
        companyRepo.updateUsingApplicationDetails(fields)

    return company_id


def post_add_application(session, user_id, applicationsRepo, companyRepo, application_form):
    # Lets get the company_id:
    company_id = add_or_update_company(user_id, application_form, companyRepo, applicationsRepo)

    # Lets add these fields to our function that will structure this data into a dict:
    application_id = add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, application_form, company_id)

    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)
