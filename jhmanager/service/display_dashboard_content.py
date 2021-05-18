from flask import Flask, render_template, session, flash
from datetime import datetime, date, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_job_offer
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_fields
from jhmanager.service.cleanup_files.cleanup_datetime_display import present_dated
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_application_fields
from jhmanager.service.cleanup_files.cleanup_general_fields import get_count


def get_users_stats(user_id, interviewsRepo, applicationsRepo, companyRepo, jobOffersRepo):
    applications = applicationsRepo.getAllApplicationsByUserID(user_id)
    interviews = interviewsRepo.getInterviewsByUserID(user_id)
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)
    
    users_stats = {
        "application_count": None, 
        "interviews_count": None, 
        "job_offers_count": None,
        "all_tables_empty": False,
    }

    if not applications and not interviews and not job_offers:
        users_stats["all_tables_empty"] = True
        return users_stats

    app_count = get_count(applications)
    if app_count >= 1:
        users_stats["application_count"] = app_count

    interview_count = get_count(interviews)
    if interview_count >= 1:
        users_stats["interviews_count"] = interview_count

    job_offers_count = get_count(job_offers)
    if job_offers_count >= 1:
        users_stats["job_offers_count"] = job_offers_count

    return users_stats
    

def display_job_offers(user_id, jobOffersRepo, companyRepo):
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)

    job_offer_details = {
        "empty_table": True,
        "fields": None
    }
    offer_count = 0

    if not job_offers:
        return job_offer_details

    job_offer_details["fields"] =  {}
    job_offer_details["empty_table"] = False

    for offer in job_offers: 
        offer_count += 1
        job_offer_id = offer.job_offer_id
        company = companyRepo.getCompanyById(offer.company_id)
        application_id = offer.application_id
        entry_date_obj = datetime.strptime(offer.entry_date, "%Y-%m-%d")
        present_dated_offer =  present_dated(entry_date_obj)

        job_offer_details["fields"][offer_count] = {
            "job_offer_id": job_offer_id,
            "starting_date": offer.starting_date, 
            "company_name": company.name,
            "job_role": offer.job_role, 
            "offer_response": offer.offer_response,
            "offer_accepted": False,
            "salary_offered": offer.salary_offered, 
            "perks_offered": offer.perks_offered,
            "present_dated_offer": present_dated_offer,
            "view_offer": '/applications/{}/job_offers/{}'.format(application_id, job_offer_id), 
        }
        cleanup_job_offer(job_offer_details, offer_count)
    
    return job_offer_details


def display_upcoming_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo):
    all_interviews = interviewsRepo.getInterviewsByUserID(user_id)
    current_date = datetime.now().date()

    upcoming_interviews = {
        "empty_table": True, 
        "fields": {}
    }

    interviews_list = {}
    if all_interviews: 
        for interview in all_interviews:
            interview_id = interview.interview_id
            application = applicationsRepo.getApplicationByID(interview.application_id)
            company = companyRepo.getCompanyById(application.company_id)
            interview_date = interview.interview_date
            interview_time = interview.interview_time
            past_dated_interview = past_dated(interview.interview_date, interview.interview_time)
            other_medium = interview.other_medium

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
                    "contact_number": interview.contact_number,
                    "interviewers": interview.interviewer_names,
                    "job_role": application.job_role,
                    "interview_today": False,
                    "view_interview": '/applications/{}/interview/{}'.format(application.app_id, interview_id), 
                }
                cleanup_interview_fields(upcoming_interviews, interview_id, other_medium)

    return upcoming_interviews


def display_today_interviews(user_id, applicationsRepo, interviewsRepo, companyRepo):
    interviews = interviewsRepo.getInterviewsByUserID(user_id)

    todays_interviews = {
        "empty_table": True, 
        "fields": {}
    }

    if not interviews:
        return todays_interviews

    for interview in interviews:
        interview_id = interview.interview_id
        application = applicationsRepo.getApplicationByID(interview.application_id)
        company = companyRepo.getCompanyById(application.company_id)
        interview_date = interview.interview_date
        present_day_interview = present_dated(interview_date)

        if not present_day_interview:
            continue

        todays_interviews["empty_table"] = False 
        other_medium = interview.other_medium
        todays_interviews["fields"][interview_id] = {
            "date": interview_date, 
            "time": interview.interview_time,
            "company_name": company.name,
            "location": interview.location,
            "status": interview.status,
            "interview_type": interview.interview_type,
            "interview_medium": interview.medium, 
            "contact_number": interview.contact_number,
            "interviewers": interview.interviewer_names,
            "job_role": application.job_role,
            "interview_today": False,
            "view_interview": '/applications/{}/interview/{}'.format(application.app_id, interview_id), 
        }
        cleanup_interview_fields(todays_interviews, interview_id, other_medium)

    return todays_interviews

def display_applications_added_today(user_id, current_date, applicationsRepo, companyRepo):
    applications = applicationsRepo.getAllApplicationsByUserID(user_id)

    todays_applications = {
        "empty_table": True, 
        "fields": {}
    }

    if not applications:
        return todays_applications

    for application in applications:
        application_id = application.app_id
        app_datetime = datetime.strptime(application.app_date, "%Y-%m-%d") 
        app_date = app_datetime.date()
        present_date = present_dated(app_date)
        company = companyRepo.getCompanyById(application.company_id)

        if not present_date: 
            continue

        todays_applications["empty_table"] = False
        todays_applications["fields"][application_id] = {
            "company_name": company.name,
            "app_date": application.app_date,
            "job_role": application.job_role,
            "emp_type": application.employment_type,
            "salary": application.salary,
            "presentation_str": None,
            "interview_stage": application.interview_stage,
            "view_application": '/applications/{}'.format(application_id)
        }
        cleanup_application_fields(todays_applications, application_id)

    return todays_applications


# This function will check if all the tables, to be presented at the top of the dashboard, are empty:
# (This would be true for a new user)
def check_if_all_tables_empty(todays_interviews, job_offer_details, upcoming_interviews, applications_added_today):
    if not todays_interviews and not job_offer_details and not upcoming_interviews and not applications_added_today: 
        return True

    return False


def create_dashboard_content(user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo, jobOffersRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = current_date = datetime.now().date()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    job_offer_details = display_job_offers(user_id, jobOffersRepo, companyRepo)
    upcoming_interviews = display_upcoming_interviews(user_id, interviewsRepo, applicationsRepo, companyRepo)

    # Now to grab the current-day's information we'll be displaying at the top of the dashboard:
    applications_added_today = display_applications_added_today(user_id, current_date, applicationsRepo, companyRepo)

    # Lets grab any interviews that the user has today:
    todays_interviews = display_today_interviews(user_id, applicationsRepo, interviewsRepo, companyRepo)

    # Now to gather the user's overall/total stats so far:
    user_stats = get_users_stats(user_id, interviewsRepo, applicationsRepo, companyRepo, jobOffersRepo)

    all_tables_empty = check_if_all_tables_empty(todays_interviews, job_offer_details, upcoming_interviews, applications_added_today)

    message = "All good!"

    display = {
        "applications_added_today": applications_added_today,
        "todays_interviews": todays_interviews, 
        "message": message,
        "upcoming_interviews": upcoming_interviews,
        "job_offer_details": job_offer_details,
        "users_stats": user_stats,
        "add_application_url": '/add_job_application',
        "all_tables_empty": all_tables_empty,
    }

    return render_template("dashboard.html", display=display)