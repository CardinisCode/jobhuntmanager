from flask import Flask, render_template, session, request
import datetime

def grab_users_application_and_add_to_sql_database(session, user_id, applicationsRepo):
    todays_date = datetime.date.today()

    employment_type = request.form.get("employment_type")
    location = request.form.get("location")
    job_description = request.form.get("job_description")
    user_notes = request.form.get("user_notes")
    job_role = request.form.get("job_role")
    company_name = request.form.get("company_name")
    platform = request.form.get("platform")
    job_perks = request.form.get("job_perks")
    company_description_on_spec = request.form.get("company_description")
    tech_stack = request.form.get("tech_stack")
    job_url = request.form.get("job_url")

    if not employment_type:
        employment_type = "N/A"
    
    if not location:
        location = "N/A"

    if not job_description:
        job_description = "N/A"

    if not user_notes:
        user_notes = "N/A"    

    if not company_name:
        company_name = "N/A"   

    if not platform:
        platform = "N/A"  

    if not job_perks:
        job_perks = "N/A"

    if not company_description_on_spec:
        company_description_on_spec = "N/A"

    if not tech_stack:
        tech_stack = "N/A"

    if not job_url:
        job_url = "N/A"

    if not job_role:
        job_role = "N/A"

    interview_stage = "N/A"
    contact_received = "N/A"

    applicationsRepo.insertApplicationDetailsToApplicationHistory(user_id, todays_date, employment_type, location, job_description, user_notes, job_role, company_name, platform, job_perks, company_description_on_spec, tech_stack, job_url, interview_stage, contact_received)

    return 

