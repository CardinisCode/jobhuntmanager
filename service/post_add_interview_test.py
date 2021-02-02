from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def add_fields_to_details_dict(company_name, job_role, emp_type, job_ref, company_spec, job_spec, perks, tech_stack, location, salary, user_notes, platform, job_url):
    details = {}
    # Gather all fields to be displayed to user as confirmation:

    details["company_name"] = {
        "label": company_name.label,
        "data": company_name.data
    }

    details["job_role"] = {
        "label": job_role.label, 
        "data": job_role.data
    }

    details["emp_type"] = {
        "label": emp_type.label, 
        "data": emp_type.data
    }

    details["job_ref"] = {
        "label": job_ref.label, 
        "data": job_ref.data
    }

    details["company_spec"] = {
        "label": company_spec.label, 
        "data": company_spec.data
    }

    details["job_spec"] = {
        "label": job_spec.label, 
        "data": job_spec.data
    }

    details["perks"] = {
        "label": perks.label, 
        "data": perks.data
    }

    details["tech_stack"] = {
        "label": tech_stack.label, 
        "data": tech_stack.data
    }

    details["tech_stack"] = {
        "label": tech_stack.label, 
        "data": tech_stack.data
    }

    details["location"] = {
        "label": location.label, 
        "data": location.data
    }

    details["salary"] = {
        "label": salary.label, 
        "data": salary.data
    }

    details["user_notes"] = {
        "label": user_notes.label, 
        "data": user_notes.data
    }

    details["platform"] = {
        "label": platform.label, 
        "data": platform.data
    }

    details["job_url"] = {
        "label": job_url.label, 
        "data": job_url.data
    }

    return details



def post_add_application_test(session, user_id, interviewsRepo, form):
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

    return render_template("applications_details_test.html", details=details)