from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime

def add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, application_form, company_id):
#    date_posted, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url, 
   
    # We need to grab current day's date & time when user adds a new application:
    # application_date = str(datetime.date(datetime.now()))
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
    data_posted_data = application_form.date_posted.data

    # Since these are optional fields for the user, 
    # lets make sure each field actually has data to insert into the db:
    emp_type = application_form.emp_type.data
    if not emp_type:
        emp_type = "N/A"

    job_ref = application_form.job_ref.data
    if not job_ref:
        job_ref = "N/A"

    company_spec = application_form.company_description.data
    if not company_spec:
        company_spec = "N/A"

    job_spec = application_form.job_description.data
    if not job_spec:
        job_spec = "N/A"

    perks = application_form.job_perks.data
    if not perks:
        perks = "N/A"    

    tech_stack = application_form.tech_stack.data
    if not tech_stack:
        tech_stack = "N/A" 

    location = application_form.location.data
    if not location:
        location = "N/A" 

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


    # Now we finish off by adding the details into the SQL db:
    fields = (job_role, app_date_str, app_time_str, data_posted_data, emp_type, job_ref, job_spec, tech_stack, perks, platform, location, salary, user_notes, job_url, user_id, company_id)
    applicationsRepo.addApplicationToHistory(fields)

    return True


def add_or_update_company(user_id, application_form, companyRepo, applicationsRepo):
    #Grab fields from form:
    company_name = application_form.company_name.data
    company_spec = application_form.company_description.data
    location = application_form.location.data
    industry = application_form.industry.data

    existing_company = companyRepo.grabCompanyByNameAndUserID(company_name, user_id)

    if not existing_company:
        flash("Save this business as a brand new business in CompanyRepo.")
        company_id = companyRepo.create(company_name, company_spec, location, industry, user_id)

    else:
        company_id = existing_company.company_id
        companyRepo.updateUsingApplicationDetails(company_name, company_spec, location, industry, user_id)
        flash("This business already exists in the DB for this user. Details have been updated.")

    return company_id


def add_fields_to_details_dict(application_form):
    # company_name, job_role, emp_type, date_posted, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url)
    
    # Add all fields & add to our display dict:
    details = {
        "company_name": {
            "label": application_form.company_name.label,
            "data": application_form.company_name.data
        }, 
        "job_ref": {
            "label": application_form.job_ref.label,
            "data": application_form.job_ref.data
        },
        "job_role": {
           "label": application_form.job_role.label, 
            "data": application_form.job_role.data
        },
        "Date Posted": {
            "label": application_form.date_posted.label, 
            "data": application_form.date_posted.data
        },
        "company_spec": {
            "label": application_form.company_description.label,
            "data": application_form.company_description.data
        },
        "job_spec": {
            "label": application_form.job_description.label, 
            "data": application_form.job_description.data
        },
        "perks": {
            "label": application_form.job_perks.label,
            "data": application_form.job_perks.data
        },
        "tech_stack": {
            "label": application_form.tech_stack.label, 
            "data": application_form.tech_stack.data
        },
        "location": {
            "label": application_form.location.label, 
            "data": application_form.location.data
        },
        "salary": {
            "label": application_form.salary.label, 
            "data": application_form.salary.data
        },
        "user_notes": {
            "label": application_form.user_notes.label, 
            "data": application_form.user_notes.data
        },
        "platform": {
            "label": application_form.platform.label, 
            "data": application_form.platform.data
        },
        "job_url": { 
            "label": application_form.job_url.label, 
            "data": application_form.job_url.data
        },
    }

    # Let's clean up the data so it displays better to the user:
    emp_type_data = application_form.emp_type.data
    if emp_type_data == "full_time":
        emp_type_data = "Full Time"

    elif emp_type_data == "part_time":
        emp_type_data = "Part Time"

    elif emp_type_data == "temp":
        emp_type_data = "Temporary"

    elif emp_type_data == "contract":
        emp_type_data = "Contract"
    
    else:
        emp_type_data = "Other"

    details["emp_type"] = {
        "label": application_form.emp_type.label, 
        "data": emp_type_data
    }

    return details


def post_add_application(session, user_id, applicationsRepo, companyRepo, application_form):
    # Lets get the company_id:
    company_id = add_or_update_company(user_id, application_form, companyRepo, applicationsRepo)

    # Lets add these fields to our function that will structure this data into a dict:
    details =  add_fields_to_details_dict(application_form)
    add_new_application_to_application_history(user_id, companyRepo, applicationsRepo, application_form, company_id)

    return render_template("application_details.html", details=details)


