from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime

def add_new_company_to_application_history(user_id, companyRepo, applicationsRepo, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url, company_id):
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
    fields = (job_role, app_date_str, app_time_str, emp_type, job_ref, company_spec, job_spec, tech_stack, perks, platform, location, salary, user_notes, job_url, user_id, company_id)
    applicationsRepo.addApplicationToHistory(fields)

    return True


def updateExistingEntryForCompanyName(user_id, field_details, applicationsRepo):
    raise ValueError("Existing company. Details:", field_details)


    # return True


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


def post_add_application(session, user_id, applicationsRepo, companyRepo, form):
    field_details = []
    
    #Grab fields from form:
    company_name = form.company_name 
    field_details.append(company_name.data)

    job_role = form.job_role
    field_details.append(job_role.data)

    emp_type = form.emp_type
    field_details.append(emp_type.data)

    job_ref = form.job_ref
    field_details.append(job_ref.data)

    company_spec = form.company_description
    field_details.append(company_spec.data)

    job_spec = form.job_description
    field_details.append(job_spec.data)

    perks = form.job_perks
    field_details.append(perks.data)

    tech_stack = form.tech_stack
    field_details.append(tech_stack.data)

    location = form.location
    field_details.append(location.data)

    salary = form.salary
    field_details.append(salary.data)

    user_notes = form.user_notes  
    field_details.append(user_notes.data)

    platform = form.platform 
    field_details.append(platform.data)

    job_url = form.job_url
    field_details.append(job_url.data)

    industry = form.industry.data

    company_id = companyRepo.create(company_name.data, company_spec.data, location.data, industry, user_id)
    # Lets add these fields to our function that will structure this data into a dict:
    details =  add_fields_to_details_dict(company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url)
    add_new_company_to_application_history(user_id, companyRepo, applicationsRepo, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url, company_id)

    # Now we want a condition:
    # If company_name already exists in application_history for this user:
    # existing_company = applicationsRepo.checkCompanyNameInApplicationHistoryByUserID(company_name.data, user_id,)
    # for item in existing_company:
    #     if item[0] == 0:
    #         add_new_company_to_application_history(user_id, applicationsRepo, company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url)
    #     else:
    #         # updateExistingEntryForCompanyName(user_id, field_details, applicationsRepo)
    #         message = "An application entry already exists for {}. Consider updating the details for this company.".format(company_name.data)
    #         flash(message)
    #         app_updated = updateApplicationEntryUsingNewApplicationDetails(field_details, user_id, applicationsRepo)
    #         raise ValueError("App updated: ", app_updated)

    return render_template("application_details.html", details=details)


