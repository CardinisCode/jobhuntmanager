from flask import Flask, render_template, session, request, redirect
from jhmanager.forms.add_application_form import AddApplicationForm


def display_update_application_form(session, user_id, application_id, update_form, company):

    fields = {
        "Company Name": company.name,
        "application_id": application_id
    }

    return render_template("update_application.html", fields=fields, update_form=update_form)