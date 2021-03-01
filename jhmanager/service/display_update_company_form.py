from flask import Flask, render_template, session, request, redirect


def display_update_company_details_form(update_form, company):
    # name = update_form.company_name.data

    details = {
        "company_name": company.name
    }
    
    return render_template("update_company.html", update_form=update_form, details=details)
