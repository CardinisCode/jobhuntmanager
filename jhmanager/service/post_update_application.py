from flask import Flask, render_template, session, request, redirect, flash


def update_application_details_from_form(session, user_id, update_form, application_id, applicationsRepo, companyRepo):
    raise ValueError("Updating application details....")