from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from datetime import datetime, date


def cleanup_offer_response(offer_response, company_name):
    updated_offer_response = ""
    if offer_response == 'user_accepted':
        updated_offer_response = "Offer Accepted!"
    elif offer_response == 'user_declined':
        updated_offer_response = "Offer Declined."
    elif offer_response == 'company_pulled_offer':
        updated_offer_response = "{} pulled the offer.".format(company_name)
    else:
        updated_offer_response = "Still deciding..."

    return updated_offer_response


def cleanup_job_offer(job_offers_details, count):
    company_name = job_offers_details["fields"][count]["company_name"]
    offer_response = job_offers_details["fields"][count]["offer_response"]
    job_offers_details["fields"][count]["offer_response"] = cleanup_offer_response(offer_response, company_name)

    starting_date = job_offers_details["fields"][count]["starting_date"]
    job_offers_details["fields"][count]["starting_date"] = cleanup_date_format(starting_date)

    offer_accepted = job_offers_details["fields"][count]["offer_accepted"]
    if offer_response == "user_accepted" or offer_response == "Offer Accepted!":
        offer_accepted = True
        job_offers_details["fields"][count]["offer_accepted"] = offer_accepted






