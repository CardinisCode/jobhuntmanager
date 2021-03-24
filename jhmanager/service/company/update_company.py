from flask import Flask, render_template, session, request, redirect, flash


def display_update_company_profile_form(company_id, update_company_form, company):
    action_url = '/company/{}/update_company'.format(company_id)

    details = {
        "company_name": company.name, 
        "action_url": action_url
    }
    
    return render_template("update_company_profile.html", update_company_form=update_company_form, details=details)



def post_update_company_profile(company_id, user_id, update_form, company, applicationsRepo, companyRepo):
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