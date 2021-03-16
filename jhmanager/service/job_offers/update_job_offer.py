from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_job_offer_form(user_id, job_offer_id, update_job_offer, companyRepo):


    details = {
        "action_url": 'job_offer/{}/update_job_offer'.format(job_offer_id)
    }

    return render_template("update_job_offer.html", update_job_offer=update_job_offer, details=details)