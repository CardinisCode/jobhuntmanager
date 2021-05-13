from flask import Flask, render_template, session, request, redirect


def display_update_application_form(session, user_id, application_id, update_form, company):
    fields = {
        "Company Name": company.name,
        "application_id": application_id, 
        "update_url": '/applications/{}/update_application'.format(application_id)
    }

    return render_template("update_application.html", fields=fields, update_form=update_form)


def post_update_application(session, user_id, update_form, application_id, company_id, applicationsRepo, companyRepo):

    # Fields to be inserted into the 'job_application' table:
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

    # Fields to be inserted into the 'company' table:
    company_details = {
        "name" : update_form.company_name.data, 
        "description" : update_form.company_description.data, 
        "industry" : update_form.industry.data, 
        "location" : update_form.location.data, 
        "user_id" : user_id, 
        "company_id": company_id
    }
    
    companyRepo.updateCompanyByApplication(company_details)
    
    # Finally once all details have been updated, 
    # we want to direct the user back to the current application:
    redirect_url = "/applications/{}".format(application_id)

    return redirect(redirect_url)