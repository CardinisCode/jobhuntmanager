from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def format_data_and_add_to_sql_db(user_id, applicationsRepo, company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url):
    # We need to grab current day's date when user adds a new application:
    # application_date = str(datetime.date(datetime.now()))
    application_date = datetime.now()

    # Before we add the fields to our SQL db, lets make sure we first grab the data for each field:
    company_name = company_name.data
    job_role = job_role.data

    # Since these are optional fields for the user, 
    # lets make sure each field actually has data to insert into the db:
    emp_type = emp_type.data
    if not emp_type:
        emp_type = "N/A"

    job_ref = job_ref.data
    if not job_ref:
        job_ref = "N/A"

    company_spec = company_spec.data
    if not company_spec:
        company_spec = "N/A"

    job_spec = job_spec.data
    if not job_spec:
        job_spec = "N/A"

    perks = perks.data
    if not perks:
        perks = "N/A"    

    tech_stack = tech_stack.data
    if not tech_stack:
        tech_stack = "N/A" 

    location = location.data
    if not location:
        location = "N/A" 

    salary = salary.data
    if not salary:
        salary = "N/A" 

    user_notes = user_notes.data
    if not user_notes:
        user_notes = "N/A" 

    platform = platform.data
    if not platform:
        platform = "N/A"     

    job_url = job_url.data
    if not job_url:
        job_url = "N/A" 

    # Now we finish off by adding the details into the SQL db:
    insert_application_details = applicationsRepo.addApplicationToHistory(company_name, job_role, application_date, emp_type, job_ref, company_spec, job_spec, tech_stack, perks, platform, location, salary, user_notes, job_url)

    # Let's verify if we've successfully added our fields to the db table:
    if not insert_application_details:
        flash("Failed to insert details into ApplicationsHistoryRepo. Please investigate!")
        return False

    return True


def add_fields_to_details_dict(company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url):
    # Add all fields & add to our display dict:
    details = {
        "company_name": {
            "label": company_name.label,
            "data": company_name.data
        }, 
        "job_role": {
           "label": job_role.label, 
            "data": job_role.data
        },
        "job_ref": {
            "label": job_ref.label,
            "data": job_ref.data
        },
        "company_spec": {
            "label": company_spec.label,
            "data": company_spec.data
        },
        "job_spec": {
            "label": job_spec.label, 
            "data": job_spec.data
        },
        "perks": {
            "label": perks.label,
            "data": perks.data
        },
        "tech_stack": {
            "label": tech_stack.label, 
            "data": tech_stack.data
        },
        "location": {
            "label": location.label, 
            "data": location.data
        },
        "salary": {
            "label": salary.label, 
            "data": salary.data
        },
        "user_notes": {
            "label": user_notes.label, 
            "data": user_notes.data
        },
        "platform": {
            "label": platform.label, 
            "data": platform.data
        },
        "job_url": { 
            "label": job_url.label, 
            "data": job_url.data
        },
    }

    # Let's clean up the data so it displays better to the user:
    emp_type_data = emp_type.data
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
        "label": emp_type.label, 
        "data": emp_type_data
    }

    return details


def post_add_application(session, user_id, applicationsRepo, form):
    #Grab fields from form:
    company_name = form.company_name 
    job_role = form.job_role
    emp_type = form.emp_type
    job_ref = form.job_ref
    company_spec = form.company_description
    job_spec = form.job_description
    perks = form.job_perks
    tech_stack = form.tech_stack
    location = form.location
    salary = form.salary
    user_notes = form.user_notes   
    platform = form.platform 
    job_url = form.job_url

    # Lets add these fields to our function that will structure this data into a dict:
    details =  add_fields_to_details_dict(company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url)

    # Add details to SQL
    format_data_and_add_to_sql_db(user_id, applicationsRepo, company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url)
    # Create function to add details to SQL table

    return render_template("application_details.html", details=details)


