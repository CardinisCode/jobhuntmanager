from flask import Flask, render_template, session, request, redirect, flash


def display_update_company_details_form(update_form, company, application):
    application_id = application.app_id

    details = {
        "company_name": company.name, 
        "application_id": application_id
    }
    
    return render_template("update_company.html", update_form=update_form, details=details)


def post_update_company(update_form, user_id, company, applicationsRepo, companyRepo, application):
    company_id = company.company_id
    application_id = application.app_id
    
    company_details = {
        "name": update_form.name.data, 
        "description": update_form.description.data,
        "industry": update_form.industry.data, 
        "location": update_form.location.data,
        "url": update_form.url.data,
        "interviewers": update_form.interviewers.data,
        "contact_number": update_form.contact_number.data,
        "user_id": user_id, 
        "company_id": company_id
    }

    companyRepo.updateByID(company_details)

    redirect_url = '/company/{}/view_company'.format(company_id)
    flash("Company Details updated!")
    return redirect(redirect_url)