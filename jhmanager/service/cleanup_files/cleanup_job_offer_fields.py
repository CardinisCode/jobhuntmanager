from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from datetime import datetime, date
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_field_value


def cleanup_offer_response(offer_response, company_name):
    updated_offer_response = ""
    if offer_response == 'user_accepted':
        updated_offer_response = "Offer Accepted!"
    elif offer_response == 'user_declined':
        updated_offer_response = "Offer Declined."
    elif offer_response == 'company_pulled_offer':
        updated_offer_response = "{} pulled the offer.".format(cleanup_field_value(company_name))
    else:
        updated_offer_response = "Still deciding..."

    return updated_offer_response


def cleanup_specific_job_offer(job_offer_details):
    company_name = job_offer_details["company_name"]

    for heading, value in job_offer_details.items():
        if heading == "starting_date":
            job_offer_details[heading] = cleanup_date_format(value)
        elif heading == "offer_response":
            job_offer_details[heading] = cleanup_offer_response(value, company_name)
        elif heading == "company_name" or heading == "job_role":
            job_offer_details[heading] = cleanup_field_value(value)
        else:
            continue


def cleanup_job_offer(job_offers_details, count):
    # We'll need the 'company_name' value declared before we update the value for the key 'offer_response'.
    company_name = job_offers_details["fields"][count]["company_name"]

    for heading, value in job_offers_details["fields"][count].items():
        if heading == "offer_response":
            job_offers_details["fields"][count][heading] = cleanup_offer_response(value, company_name)
            
            # If the user has accepted the job offer, we can upate the dictionary's key: 'offer_accepted'
            if value == "Offer Accepted!":
                job_offers_details["fields"][count]["offer_accepted"] = True
        elif heading == "starting_date":
            job_offers_details["fields"][count][heading] = cleanup_date_format(value)
        elif heading == "company_name" or heading == "job_role":
            job_offers_details["fields"][count][heading] = cleanup_field_value(value)
        else:
            continue
