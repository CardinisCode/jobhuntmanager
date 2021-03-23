from flask import Flask, render_template, session, request, redirect, flash
import sqlite3


def display_add_company_form(add_company_form):
    details = {
        "action_url": '/add_company'
    }
    
    return render_template("add_company_form.html", add_company_form=add_company_form, details=details)


def post_add_company(user_id, add_company_form, applicationsRepo, companyRepo):
    # (user_id, name, description, location, industry, url, interviewers, contact_number)
    company_details = {
        "user_id": user_id, 
        "name": add_company_form.name.data, 
        "description": add_company_form.description.data,
        "location": add_company_form.location.data,
        "industry": add_company_form.industry.data, 
        "url": add_company_form.url.data,
        "interviewers": add_company_form.interviewers.data,
        "contact_number": add_company_form.contact_number.data,
    }

    company_id = companyRepo.createCompany(company_details)

    redirect_url = '/company/{}/view_company'.format(company_id)
    flash("Company Details updated!")
    return redirect(redirect_url)