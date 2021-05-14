from flask import Flask, render_template, session, request, redirect, flash


def delete_job_offer_entry(application_id, job_offer_id, jobOffersRepo):
    jobOffersRepo.deleteJobOfferByID(job_offer_id)

    flash("Job Offer successfully deleted.")

    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)