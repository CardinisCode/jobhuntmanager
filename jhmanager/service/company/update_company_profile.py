from flask import Flask, render_template, session, request, redirect, flash


def display_update_company_profile_form(update_form, company):
    company_id = company.company_id
    action_url = '/company/{}/update_company'.format(company_id)

    details = {
        "company_name": company.name, 
        "action_url": action_url
    }
    
    return render_template("update_company.html", update_form=update_form, details=details)