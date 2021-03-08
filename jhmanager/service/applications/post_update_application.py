from flask import Flask, render_template, session, request, redirect, flash


def update_application_details_from_form(session, user_id, update_form, application_id, company_id, applicationsRepo, companyRepo):

    # application details:
    application_fields = {
        "job_role": update_form.job_role.data, 
        "employment_type": update_form.emp_type.data,
        "job_ref": update_form.job_ref.data, 
        "job_description": update_form.job_description.data, 
        "job_perks": update_form.job_perks.data,
        "tech_stack": update_form.tech_stack.data,
        "salary": update_form.salary.data,
        "user_notes" : update_form.user_notes.data, 
        "platform" : update_form.platform.data,
        "job_url" : update_form.job_url.data,
        "application_id": application_id, 
    }

    applicationsRepo.updateApplicationByID(application_fields)

    # Company details:
    company_details = {
        "name" : update_form.company_name.data, 
        "description" : update_form.company_description.data, 
        "industry" : update_form.industry.data, 
        "location" : update_form.location.data, 
        "user_id" : user_id, 
        "company_id": company_id
    }
    
    companyRepo.updateUsingApplicationDetails(company_details)
    
    # Finally once all details have been updated, 
    # we want to direct the user back to the current application:
    redirect_url = "/applications/{}".format(application_id)

    return redirect(redirect_url)