from flask import Flask, render_template, session, flash
from datetime import datetime, date, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_job_offer
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_fields
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_status
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_type
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_upcoming_interview_fields
from jhmanager.service.cleanup_files.cleanup_interview_fields import check_interview_is_today


def extract_and_display_job_offers(user_id, jobOffersRepo, companyRepo):
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)

    job_offer_details = {
        "offer_count": 0, 
        "fields": None
    }
    offer_count = 0
    count_list = []

    if not job_offers: 
        return job_offer_details

    job_offer_details = {"fields": {}}
    for offer in job_offers: 
        offer_count += 1
        count_list.append(offer_count)
        job_offer_id = offer.job_offer_id
        company_id = offer.company_id
        application_id = offer.application_id
        company_name = companyRepo.getCompanyById(company_id).name
        view_offer_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)

        job_offer_details["fields"][offer_count] = {
            "job_offer_id": job_offer_id,
            "starting_date": offer.starting_date, 
            "company_name": company_name,
            "job_role": offer.job_role, 
            "offer_response": offer.offer_response,
            "offer_accepted": False,
            "salary_offered": offer.salary_offered, 
            "perks_offered": offer.perks_offered,
            "view_offer_url": view_offer_url, 
        }
        cleanup_job_offer(job_offer_details, offer_count)

    job_offer_details["offer_count"] = offer_count

    return job_offer_details


def display_upcoming_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo):
    all_interviews = interviewsRepo.grabUpcomingInterviewsByUserID(user_id)
    current_date = datetime.now().date()

    upcoming_interviews = {
        "empty_table": True, 
        "fields": {}
    }

    if all_interviews: 
        for interview in all_interviews:
            interview_id = interview.interview_id
            application = applicationsRepo.grabApplicationByID(interview.application_id)
            company = companyRepo.getCompanyById(application.company_id)
            interview_date = interview.interview_date
            interview_time = interview.interview_time
            past_dated_interview = past_dated(interview.interview_date, interview.interview_time)

            if not past_dated_interview:
                upcoming_interviews["empty_table"] = False 
                upcoming_interviews["fields"][interview_id] = {
                    "date": interview_date, 
                    "time": interview_time,
                    "company_name": company.name,
                    "location": interview.location,
                    "status": interview.status,
                    "interview_type": interview.interview_type,
                    "interview_medium": interview.medium, 
                    "other_medium": interview.other_medium,
                    "contact_number": interview.contact_number,
                    "interviewers": interview.interviewer_names,
                    "job_role": application.job_role,
                    "interview_today": False,
                    "interview_string": None,
                    "view_interview": '/applications/{}/interview/{}'.format(application.app_id, interview_id), 
                }
                cleanup_upcoming_interview_fields(upcoming_interviews, interview_id)

    return upcoming_interviews


def get_application_count(applications):
    app_count = 0
    if not applications: 
        return app_count

    for application in applications:
        app_count += 1

    return app_count


def display_todays_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo):
    current_date = datetime.now().date()
    interviews = interviewsRepo.grabAllInterviewsForUserID(user_id)
    
    todays_interviews_details = {
        "empty_table": True, 
        "fields": {}
    }

    if interviews: 
        for interview in interviews:
            interview_id = interview.interview_id
            application = applicationsRepo.grabApplicationByID(interview.application_id)
            company = companyRepo.getCompanyById(application.company_id)
            interview_date = interview.interview_date
            interview_time = interview.interview_time
            present_day_interview = check_interview_is_today(interview_date)

            # We only want to add interviews that are actually dated 'today'. 
            if present_day_interview:
                todays_interviews_details["empty_table"] = False 
                todays_interviews_details["fields"][interview_id] = {
                    "date": interview_date, 
                    "time": interview_time,
                    "company_name": company.name,
                    "location": interview.location,
                    "status": interview.status,
                    "interview_type": interview.interview_type,
                    "interview_medium": interview.medium, 
                    "other_medium": interview.other_medium,
                    "contact_number": interview.contact_number,
                    "interviewers": interview.interviewer_names,
                    "job_role": application.job_role,
                    "interview_today": False,
                    "interview_string": None,
                    "view_interview": '/applications/{}/interview/{}'.format(application.app_id, interview_id), 
                }
                cleanup_upcoming_interview_fields(todays_interviews_details, interview_id)

    return todays_interviews_details


def create_dashboard_content(user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo, jobOffersRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    job_offer_details = extract_and_display_job_offers(user_id, jobOffersRepo, companyRepo)

    # Now to grab the figures/stats we'll be displaying at the top of the dashboard:
    applications_today = applicationsRepo.grabTodaysApplicationCount(date_str, user_id)
    all_applications = applicationsRepo.getAllApplicationsByUserID(user_id)
    interviews_today = display_todays_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo)
    upcoming_interviews = display_upcoming_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo)

    # Sadly SQLite doesn't have the functionality to return COUNT(*) from SQLite to Python
    # So we'll have manually count the number of rows returned from the SQL query:
    today_app_count = get_application_count(applications_today)
    all_app_count = get_application_count(all_applications)

    message = "All good!"

    display = {
        'current_date': current_date,
        "applications_today": today_app_count,
        "interviews_today": interviews_today,
        "job_offer_count": job_offer_details["offer_count"],
        "message": message,
        "upcoming_interviews": upcoming_interviews,
        "job_offer_details": job_offer_details,
        "add_application_url": '/add_job_application',
        "total_application_count": all_app_count
    }

    return render_template("dashboard.html", display=display)