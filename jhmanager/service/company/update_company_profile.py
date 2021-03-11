from flask import Flask, render_template, session, request, redirect, flash


def display_update_company_profile_form(company_id, update_form, company):
    action_url = '/company/{}/update_company'.format(company_id)

    details = {
        "company_name": company.name, 
        "action_url": action_url
    }
    
    return render_template("update_company.html", update_form=update_form, details=details)