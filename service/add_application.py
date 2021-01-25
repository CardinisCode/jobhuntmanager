from flask import Flask, render_template, session, request, redirect
from datetime import datetime



def grab_users_application_and_add_to_sql_database(session, user_id, applicationsRepo):
    todays_date = datetime.now()
    # todays_date_and_time = todays_date.strftime("%d/%m/%y %H:%M")
    todays_date_and_time = todays_date
    # raise ValueError("Date:", todays_date_and_time, "Date type:", type(todays_date_and_time))

    employment_type = request.form.get("type_of_employment")
    location = request.form.get("location")
    job_description = request.form.get("job_description")
    salary = request.form.get("salary")
    user_notes = request.form.get("user_notes")
    job_role = request.form.get("job_role")
    company_name = request.form.get("company_name")
    platform = request.form.get("platform")
    job_perks = request.form.get("job_perks")
    company_description_on_spec = request.form.get("company_description")
    tech_stack = request.form.get("tech_stack")
    job_url = request.form.get("job_url")
    job_ref = request.form.get("job_ref")

    if not employment_type:
        employment_type = "Full Time"
    
    if not location:
        location = "Remote"

    if not job_description:
        job_description = "N/A"

    if not user_notes:
        user_notes = "N/A"    

    if not company_name:
        company_name = "Not Provided"   

    if not platform:
        platform = "N/A"  

    if not job_perks:
        job_perks = "Not Provided"

    if not company_description_on_spec:
        company_description_on_spec = "Not Provided"

    if not tech_stack:
        tech_stack = "N/A"

    if not job_url:
        job_url = "Not Provided"

    if not job_role:
        job_role = "Not Provided"

    if not job_ref:
        job_ref = "N/A"

    interview_stage = "Application submitted"
    contact_received = "No"

    applicationsRepo.insertApplicationDetailsToApplicationHistory(user_id, todays_date, employment_type, location, job_description, user_notes, job_role, company_name, platform, job_perks, company_description_on_spec, tech_stack, job_url, interview_stage, contact_received, job_ref, salary)

    if employment_type == 'full_time':
        employment_type = "Full Time"
    elif employment_type == 'part_time':
        employment_type = "Part Time"
    elif employment_type == 'temporary':
        employment_type = "Temporary"
    elif employment_type == "contract":
        employment_type = "Contracting"
    else: 
        employment_type = "Other"

    application_details = {
        "todays_date": todays_date_and_time,
        "job_ref": job_ref,
        "job_role": job_role, 
        "salary": salary,
        "job_description": job_description,
        "employment_type": employment_type,  
        "tech_stack": tech_stack, 
        "company_name": company_name, 
        "company_description": company_description_on_spec, 
        "job_perks": job_perks, 
        "location": location,
        "platform": platform, 
        "job_url": job_url,
        "user_notes":  user_notes, 
    }

    return render_template("application_details.html", application_details=application_details)

