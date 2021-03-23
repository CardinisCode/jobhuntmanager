from flask import Flask, render_template, session, request, redirect, flash


def display_add_company_form(add_company_form):
    details = {
        "action_url": '/add_company'
    }
    
    return render_template("add_company_form.html", add_company_form=add_company_form, details=details)


def post_add_company(user_id, add_company_form, applicationsRepo, companyRepo):
    company_details = {
        "name": add_company_form.name.data, 
        "description": add_company_form.description.data,
        "industry": add_company_form.industry.data, 
        "location": add_company_form.location.data,
        "url": add_company_form.url.data,
        "interviewers": add_company_form.interviewers.data,
        "contact_number": add_company_form.contact_number.data,
        "user_id": user_id, 
    }

    # company_id = 

    redirect_url = '/company/{}/view_company'.format(company_id)
    flash("Company Details updated!")
    return redirect(redirect_url)