from flask import Flask, render_template, session, flash
from datetime import datetime, date, time
from jhmanager.service.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_datetime_display import past_dated


def clean_up_job_offer_details(job_offer_details, offer_count):
    company_name = job_offer_details[offer_count]["company_name"]
    offer_response = job_offer_details[offer_count]["offer_response"]
    start_date = job_offer_details[offer_count]["starting_date"]
    message = ""
    if offer_response == 'user_accepted':
        message = "I've accepted the offer!"
    elif offer_response == 'user_declined':
        message = "I've declined the offer."
    elif offer_response == 'company_pulled_offer':
        message = "{} pulled the offer.".format(company_name)
    else:
        message = "Still deciding..."

    job_offer_details[offer_count]["offer_response"] = message
    job_offer_details[offer_count]["starting_date"] = cleanup_date_format(start_date)


def extract_and_display_job_offers(job_offers, companyRepo):
    job_offer_details = None
    offer_count = 0
    count_list = []

    if not job_offers: 
        return (job_offer_details, offer_count)

    job_offer_details = {}
    for offer in job_offers: 
        offer_count += 1
        count_list.append(offer_count)
        job_offer_id = offer.job_offer_id
        company_id = offer.company_id
        application_id = offer.application_id
        company_name = companyRepo.getCompanyById(company_id).name
        view_offer_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)

        job_offer_details[offer_count] = {
            "job_offer_id": job_offer_id,
            "starting_date": offer.starting_date, 
            "company_name": company_name,
            "job_role": offer.job_role, 
            "offer_response": offer.offer_response,
            "salary_offered": offer.salary_offered, 
            "perks_offered": offer.perks_offered,
            "view_offer_url": view_offer_url, 
        }
        clean_up_job_offer_details(job_offer_details, offer_count)


    return (job_offer_details, offer_count)


def cleanup_interview_details(interview_details, other_medium, company_name, interview_id):
    medium = interview_details[company_name][interview_id]["interview_medium"]
    interviewers = interview_details[company_name][interview_id]["interviewers"]
    interview_date = interview_details[company_name][interview_id]["Date"]
    interview_time = interview_details[company_name][interview_id]["Time"]
    past_dated_interview = past_dated(interview_date, interview_time)

    if past_dated_interview:
        interview_details[company_name][interview_id]["past_dated"] = past_dated_interview

    interview_details[company_name][interview_id]["Date"] = cleanup_date_format(interview_date)
    interview_details[company_name][interview_id]["Time"] = cleanup_time_format(interview_time)

    # Lets cleaned up the display of 'Medium':
    if medium == "google_chat":
        interview_details[company_name][interview_id]["interview_medium"] = "Google Chat"
    elif medium == "meet_jit_si":
        interview_details[company_name][interview_id]["interview_medium"] = "Meet.Jit.Si"
    elif medium == "other":
        interview_details[company_name][interview_id]["interview_medium"] = other_medium
    else: 
        interview_details[company_name][interview_id]["interview_medium"] = medium.capitalize()

    if interviewers == "Unknown at present":
        interview_details[company_name][interview_id]["interviewers"] = None

    return "Done"


def extract_and_display_interviews(all_interviews, applicationsRepo, companyRepo): 
    if not all_interviews: 
        interview_details = None
    else: 
        interview_details = {}
        for interview in all_interviews:
            interview_id = interview.interview_id
            application_id = interview.application_id
            company_id = applicationsRepo.grabApplicationByID(application_id).company_id
            company_name = companyRepo.getCompanyById(company_id).name
            view_more_url = '/applications/{}/interview/{}'.format(application_id, interview_id)
            update_url = '/applications/{}/interview/{}/update_interview'.format(application_id, interview_id)
            other_medium = interview.other_medium
            
            interview_details[company_name] = {} 
            interview_details[company_name][interview_id] = {
                "Date": interview.interview_date, 
                "Time": interview.interview_time,
                "Location": interview.location,
                "View_More": view_more_url, 
                "status": interview.status,
                "interview_type": interview.interview_type,
                "interview_medium": interview.medium, 
                "contact_number": interview.contact_number,
                "interviewers": interview.interviewer_names,
                "past_dated": False, 
                "update_url": update_url, 
                "prepare_url": '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
            }
            cleanup_interview_details(interview_details, other_medium, company_name, interview_id)


    return interview_details


def create_dashboard_content(user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo, jobOffersRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    # Now to grab the values for the Applications & Interviews added on the current date (from the perspective SQL queries):
    # Firstly: applications
    applications_today = applicationsRepo.grabTodaysApplicationCount(date_str, user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(date_str, user_id)
    # all_interviews = interviewsRepo.grabAllInterviewsForUserID(user_id)
    all_interviews = interviewsRepo.grabUpcomingInterviewsByUserID(user_id)
    interview_details = extract_and_display_interviews(all_interviews, applicationsRepo, companyRepo)

    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)
    job_offer_details = extract_and_display_job_offers(job_offers, companyRepo)[0]
    job_offer_count = extract_and_display_job_offers(job_offers, companyRepo)[1]

    # Sadly SQLite doesn't have the functionality to return COUNT(*) from SQLite to Python
    # So we'll have manually count the number of rows returned from the SQL query:
    app_today_count = 0
    for app in applications_today:
        app_today_count += 1

    interviews_today_count = 0
    for interview in interviews_today:
        interviews_today_count += 1

    message = "All good!"

    display = {
        'current_date': current_date,
        "applications_today": app_today_count,
        "interviews_today": interviews_today_count,
        "job_offer_count": job_offer_count,
        "message": message,
        "interview_details": interview_details, 
        "job_offer_details": job_offer_details,
        "add_application_url": '/add_job_application'
    }

    return render_template("dashboard.html", display=display)