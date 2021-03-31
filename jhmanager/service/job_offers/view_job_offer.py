from flask import Flask, render_template, session, request, redirect, flash


def display_job_offer(job_offer_id, jobOffersRepo, companyRepo):
    job_offer = jobOffersRepo.getJobOfferByJobOfferID(job_offer_id)
    company = companyRepo.getCompanyById(job_offer.company_id)
    company_name = company.name
    update_url = '/job_offer/{}/update_job_offer'.format(job_offer_id)
    delete_url = '/job_offer/{}/delete_job_offer'.format(job_offer_id)
    company_profile_url = '/company/{}/view_company'.format(company.company_id)

    display = {
        "company_name": company_name, 
        "job_role": job_offer.job_role, 
        "starting_date": job_offer.starting_date, 
        "salary_offered": job_offer.salary_offered, 
        "perks_offered": job_offer.perks_offered, 
        "offer_response": job_offer.offer_response, 
        "update_offer_url": update_url, 
        "delete_offer_url": delete_url, 
        "company_profile_url": company_profile_url,
    }

    return render_template("view_job_offer.html", display=display)