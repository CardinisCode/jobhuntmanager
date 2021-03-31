from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_datetime_display import cleanup_date_format


def cleanup_job_offer(job_offers_details, count):
    offer_response = job_offers_details["details"][count]["offer_response"]
    job_offers_details["details"][count]["offer_response"] = cleanup_offer_response(offer_response)

    starting_date = job_offers_details["details"][count]["starting_date"]
    job_offers_details["details"][count]["starting_date"] = cleanup_date_format(starting_date)

    offer_accepted = job_offers_details["details"][count]["offer_accepted"]
    if offer_response == "user_accepted":
        offer_accepted = True
        job_offers_details["details"][count]["offer_accepted"] = offer_accepted


def cleanup_offer_response(offer_response):
    updated_offer_response = ""
    if offer_response == 'user_accepted':
        updated_offer_response = "I've accepted the offer!"
    elif offer_response == 'user_declined':
        updated_offer_response = "I've declined the offer."
    elif offer_response == 'company_pulled_offer':
        updated_offer_response = "{} pulled the offer.".format(company_name)
    else:
        updated_offer_response = "Still deciding..."

    return updated_offer_response


def cleanup_interview_stage(interview_stage): 
    updated_interview_stage = ""
    if interview_stage == 0:
        updated_interview_stage = "No interview lined up yet."
    else:
        updated_interview_stage = "Interview #" + str(interview_stage) + "."
    
    return updated_interview_stage