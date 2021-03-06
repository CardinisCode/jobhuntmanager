import os
import sys
import logging

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_fontawesome import FontAwesome
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect

from datetime import datetime, date
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

from jhmanager.helpers_from_cs50_finance import login_required, apology

from jhmanager.repo.users import UserRepository
from jhmanager.repo.company import CompanyRepository
from jhmanager.repo.applications_history import ApplicationsHistoryRepository
from jhmanager.repo.interviews_history import InterviewsHistoryRepository
from jhmanager.repo.interview_prep_history import InterviewPreparationRepository
from jhmanager.repo.company_notes import CompanyNotesRepository
from jhmanager.repo.job_offers_history import JobOffersRepository
from jhmanager.repo.application_notes import ApplicationNotesRepository
from jhmanager.repo.contacts import ContactRepository

from jhmanager.service.users.register_user import display_register_form
from jhmanager.service.users.register_user import post_register_user
from jhmanager.service.users.user_profile import display_user_profile
from jhmanager.service.users.login_user import display_login_form
from jhmanager.service.users.login_user import post_login
from jhmanager.service.users.change_password import display_change_password_form
from jhmanager.service.users.change_password import post_change_password
from jhmanager.service.users.update_email import display_update_email_form
from jhmanager.service.users.update_email import post_update_email_address
from jhmanager.service.users.delete_user_account import display_delete_user_form
from jhmanager.service.users.delete_user_account import post_delete_user

from jhmanager.service.applications.add_application import display_add_application_form
from jhmanager.service.applications.add_application import post_add_application
from jhmanager.service.applications.delete_an_application import delete_application
from jhmanager.service.applications.update_application import display_update_application_form
from jhmanager.service.applications.update_application import post_update_application
from jhmanager.service.applications.view_application_details import display_application_details
from jhmanager.service.applications.view_all_applications import display_applications_for_user
from jhmanager.service.applications.delete_all_applications import delete_all_applications_for_user

from jhmanager.service.interviews.add_interview import display_add_interview
from jhmanager.service.interviews.add_interview import post_add_interview
from jhmanager.service.interviews.view_interview_details import display_interview_details
from jhmanager.service.interviews.update_interview import display_update_interview_form
from jhmanager.service.interviews.update_interview import post_update_interview
from jhmanager.service.interviews.delete_an_interview import delete_interview
from jhmanager.service.interviews.view_all_interviews import display_all_interviews_for_application
from jhmanager.service.interviews.update_interview_status import display_update_status_form
from jhmanager.service.interviews.update_interview_status import post_update_interview_status

from jhmanager.service.interview_preparation.add_interview_prep import display_interview_preparation_form
from jhmanager.service.interview_preparation.add_interview_prep import post_add_interview_preparation
from jhmanager.service.interview_preparation.view_interview_prep_details import display_interview_prep_details
from jhmanager.service.interview_preparation.view_all_interview_prep import display_all_interview_prep_entries
from jhmanager.service.interview_preparation.update_interview_prep import display_update_interview_prep_form
from jhmanager.service.interview_preparation.update_interview_prep import post_update_interview_preparation
from jhmanager.service.interview_preparation.delete_interview_prep import delete_interview_prep_entry

from jhmanager.service.application_notes.add_app_note import display_application_note_form
from jhmanager.service.application_notes.add_app_note import post_application_add_note
from jhmanager.service.application_notes.view_application_notes import display_application_notes
from jhmanager.service.application_notes.view_app_note_details import display_application_note_details
from jhmanager.service.application_notes.update_app_note import display_update_app_note_form
from jhmanager.service.application_notes.update_app_note import post_update_app_note
from jhmanager.service.application_notes.delete_app_note import delete_application_note

from jhmanager.service.company.add_company import display_add_company_form
from jhmanager.service.company.add_company import post_add_company
from jhmanager.service.company.update_company import display_update_company_profile_form
from jhmanager.service.company.update_company import post_update_company_profile
from jhmanager.service.company.view_all_companies import display_all_companies_for_user
from jhmanager.service.company.view_company_profile import display_company_profile
from jhmanager.service.company.add_company_job_application import display_add_company_application_form
from jhmanager.service.company.add_company_job_application import post_add_company_job_application
from jhmanager.service.company.delete_company import display_delete_company_form
from jhmanager.service.company.delete_company import post_delete_company

from jhmanager.service.company_notes.add_company_note import display_add_company_note_form
from jhmanager.service.company_notes.add_company_note import post_add_company_note
from jhmanager.service.company_notes.view_all_company_notes import display_all_notes_for_a_company
from jhmanager.service.company_notes.view_specific_note import display_company_note_details
from jhmanager.service.company_notes.update_company_note import display_update_company_note_form
from jhmanager.service.company_notes.update_company_note import post_update_company_form
from jhmanager.service.company_notes.delete_company_note import delete_specific_company_note

from jhmanager.service.job_offers.add_job_offer import display_add_job_offer_form
from jhmanager.service.job_offers.add_job_offer import post_add_job_offer
from jhmanager.service.job_offers.view_job_offer import display_job_offer
from jhmanager.service.job_offers.update_job_offer import display_update_job_offer_form
from jhmanager.service.job_offers.update_job_offer import post_update_job_offer
from jhmanager.service.job_offers.delete_job_offer import delete_job_offer_entry

from jhmanager.service.display_dashboard_content import create_dashboard_content
from jhmanager.service.display_all_notes import display_all_user_notes
from jhmanager.service.address_book.view_address_book import display_address_book

from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_offer_response

from jhmanager.service.contacts_directory.view_contact_list import display_contacts_for_user
from jhmanager.service.contacts_directory.add_new_contact import display_add_new_contact_form
from jhmanager.service.contacts_directory.add_new_contact import post_add_new_contact
from jhmanager.service.contacts_directory.view_contact_details import display_contact_details
from jhmanager.service.contacts_directory.update_contact import display_update_contact_form
from jhmanager.service.contacts_directory.update_contact import post_update_contact
from jhmanager.service.contacts_directory.delete_contact import delete_contact_details

from jhmanager.forms.add_interview_form import AddInterviewForm
from jhmanager.forms.add_application_form import AddApplicationForm
from jhmanager.forms.register_form import RegisterUserForm
from jhmanager.forms.login_form import LoginForm
from jhmanager.forms.add_interview_prep_form import AddInterviewPrepForm
from jhmanager.forms.add_company_form import AddCompanyForm
from jhmanager.forms.update_company_form import UpdateCompany
from jhmanager.forms.add_application_note_form import AddApplicationNoteForm
from jhmanager.forms.update_user_details import UpdateEmailAddressForm
from jhmanager.forms.update_user_details import ChangePasswordForm
from jhmanager.forms.delete_account_form import DeleteAccountForm
from jhmanager.forms.add_company_note_form import AddCompanyNoteForm
from jhmanager.forms.add_job_offer_form import AddJobOffer
from jhmanager.forms.warning_form import WarningForm
from jhmanager.forms.add_company_job_app_form import AddCompanyJobApplicationForm
from jhmanager.forms.delete_form import DeleteCompanyForm
from jhmanager.forms.add_new_contact_form import AddNewContactForm
from jhmanager.forms.update_interview_status_form import UpdateInterviewStatusForm


# Configure application
app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)
mail = Mail()
fa = FontAwesome(app)
bootstrap = Bootstrap(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.debug = True

# Setting up the secret key:
app.config['SECRET_KEY'] = 'a really really really really long secret key'

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure sqlite3 Library to use SQLite database
db = sqlite3.connect('jhmanager/jhmanager.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
userRepo = UserRepository(db)
companyRepo = CompanyRepository(db)
applicationsRepo = ApplicationsHistoryRepository(db)
interviewsRepo = InterviewsHistoryRepository(db)
interviewPrepRepo = InterviewPreparationRepository(db)
companyNotesRepo = CompanyNotesRepository(db)
jobOffersRepo = JobOffersRepository(db)
appNotesRepo = ApplicationNotesRepository(db)
contactRepo = ContactRepository(db)

""" Display the landing 'Home' page """
@app.route("/")
def index():
    """ Landing page that everyone sees """
    return render_template("index.html")

""" Display User Profile """
@app.route("/userprofile")
@login_required
def display_userprofile():
    """ Display User Profile """
    user_id = session["user_id"]
    return display_user_profile(user_id, userRepo)

""" Display the Register Page """
@app.route("/register", methods=["GET", "POST"])
def register_user():
    register_form = RegisterUserForm()
    if request.method == "POST":
        if register_form.validate_on_submit():
            return post_register_user(session, userRepo, register_form)
        else:
            flash("Complete all the fields.")
            return display_register_form(register_form)

    """Provide registration form to user"""
    if request.method == "GET":
        return display_register_form(register_form)

# Taken from CS50's Finance source code & modified
""" Display the Login Page """
@app.route("/login", methods=["GET", "POST"])
def test_login():
    """Log user in"""
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            app.logger.info("Successfully logged in {}".format(str(login_form.username.data)))
            return post_login(login_form, userRepo)
        else:
            flash("Complete all the fields.")
            app.logger.error("Failed to log in {}".format(login_form.errors))
            return display_login_form(login_form)

    """ Display Login form to the user """
    if request.method == "GET":
        return display_login_form(login_form)

""" Log User out of their account """
@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

""" Update User's Email """
@app.route('/userprofile/<int:user_id>/update_email', methods=["GET", "POST"])
@login_required
def update_email_address(user_id):
    user_id = session["user_id"]
    user_details = userRepo.getUserByID(user_id)
    update_email_form = UpdateEmailAddressForm(obj=user_details)

    if request.method == "POST":
        if update_email_form.validate_on_submit():
            return post_update_email_address(update_email_form, userRepo, user_id)
        else:
            flash("All fields are required.")
            return display_update_email_form(user_id, update_email_form)

    if request.method == "GET":
        return display_update_email_form(user_id, update_email_form)

""" Update User's account password """
@app.route('/userprofile/<int:user_id>/change_password', methods=["GET", "POST"])
@login_required
def change_user_password(user_id):
    user_id = session["user_id"]
    change_password_form = ChangePasswordForm()

    if request.method == "POST":
        if change_password_form.validate_on_submit() == False:
            flash("All fields are required.")
            return display_change_password_form(user_id, change_password_form)
        if change_password_form.validate_on_submit():
            return post_change_password(change_password_form, user_id, userRepo)

    if request.method == "GET":
        return display_change_password_form(user_id, change_password_form)

""" Delete User's account """
@app.route('/userprofile/<int:user_id>/delete_account', methods=["GET", "POST"])
@login_required
def delete_user_account(user_id):
    delete_account_form = DeleteAccountForm()

    if request.method == "GET":
        return display_delete_user_form(user_id, delete_account_form)
        
    if request.method == "POST":
        if delete_account_form.validate_on_submit():
            return post_delete_user(delete_account_form, user_id, userRepo, applicationsRepo, appNotesRepo, interviewPrepRepo, interviewsRepo, companyRepo, companyNotesRepo, jobOffersRepo, contactRepo)
        else:
            flash("Failed to delete the account.")
            return display_delete_user_form(user_id, delete_account_form)

""" Display the 'Dashboard' page """
@app.route("/dashboard")
@login_required
def display_dashboard():
    user_id = session["user_id"]
    return create_dashboard_content(user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo, jobOffersRepo)

""" Display the 'About Us' page """
@app.route("/about_us")
def read_about_us():
    return render_template("about_us.html")

""" View all job applications """
@app.route("/applications")
@login_required
def display_applications():
    """ Display User's Job Applications """
    user_id = session["user_id"]
    return display_applications_for_user(session, user_id, applicationsRepo, companyRepo)

""" View a specific application """
@app.route('/applications/<int:application_id>')
@login_required
def show_application(application_id):
    # Show the details for a specific application:
    user_id = session["user_id"]
    return display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo, jobOffersRepo)

""" Add a new application """
@app.route("/add_job_application", methods=["GET", "POST"])
@login_required
def add_job_application():
    add_application_form = AddApplicationForm()
    user_id = session["user_id"]

    """ Validate the details provided by user & if it passes, display details to user """
    if request.method == "POST":
        if add_application_form.validate_on_submit():
            return post_add_application(session, user_id, applicationsRepo, companyRepo, add_application_form)
        else: 
            flash("Complete all the fields.")
            return display_add_application_form(add_application_form)

    """ Display Add Job Application form to user """
    if request.method == "GET":
        return display_add_application_form(add_application_form)
        
""" Delete a specific application """
@app.route('/applications/<int:application_id>/delete', methods=["GET"])
@login_required
def delete_specific_application(application_id):
    return delete_application(application_id, applicationsRepo, interviewsRepo, interviewPrepRepo, appNotesRepo, jobOffersRepo)

""" Delete all applications """
@app.route('/applications/delete_all_applications', methods=["GET"])
@login_required
def delete_all_applications():
    user_id = session["user_id"]
    return delete_all_applications_for_user(user_id, applicationsRepo, appNotesRepo, interviewPrepRepo, interviewsRepo, jobOffersRepo)

""" Update a Specific application """
@app.route('/applications/<int:application_id>/update_application', methods=["GET", "POST"])
@login_required
def update_specific_application(application_id):
    user_id = session["user_id"]

    application_details = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application_details.company_id)
    application_details.withCompanyDetails(company)
    company_id = application_details.company_id

    # Now to instantiate the AddApplicationForm using the details for this application:
    update_form = AddApplicationForm(obj=application_details)

    # POST
    if request.method == "POST":
        if update_form.validate_on_submit():
            return post_update_application(session, user_id, update_form, application_id, company_id, applicationsRepo, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_update_application_form(session, user_id, application_id, update_form, company)

    if request.method == "GET":
        return display_update_application_form(session, user_id, application_id, update_form, company)

""" Add a Job Interview """
@app.route('/applications/<int:application_id>/add_interview', methods=["GET", "POST"])
@login_required
def add_interview(application_id):
    add_interview_form = AddInterviewForm()
    user_id = session["user_id"]

    if request.method == "POST":
        if add_interview_form.validate_on_submit():
            return post_add_interview(user_id, add_interview_form, interviewsRepo, applicationsRepo, application_id, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo)

    """ Display add_interview Form to user """
    if request.method == "GET":
        return display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo)

""" View all interviews for an application:""" 
@app.route('/applications/<int:application_id>/view_all_interviews')
@login_required
def view_all_interviews_for_application(application_id):
    return display_all_interviews_for_application(application_id, interviewsRepo, companyRepo, applicationsRepo)


""" View a specific interview: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>')
@login_required
def display_interview(application_id, interview_id):
    """ Display Interview Details for a specific interview to the user """
    user_id = session["user_id"]
    return display_interview_details(interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo)

""" Update a specific interview: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/update_interview', methods=["GET", "POST"])
@login_required
def update_specific_interview(application_id, interview_id):
    user_id = session["user_id"]
    interview_details = interviewsRepo.getInterviewByID(interview_id)
    update_interview_form = AddInterviewForm(obj=interview_details)

    if request.method == "POST":
        if update_interview_form.validate_on_submit():
            return post_update_interview(update_interview_form, application_id, interview_id, interviewsRepo)
        else:
            flash("Complete all the fields.")
            return display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo)

    if request.method == "GET":
        return display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo)

""" Update the 'Status' for a specific interview: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/update_interview_status', methods=["GET", "POST"])
@login_required
def update_interview_status(application_id, interview_id):
    update_status_form = UpdateInterviewStatusForm()
    if request.method == "GET":
        return display_update_status_form(update_status_form, application_id, interview_id, applicationsRepo, companyRepo)

    if request.method == "POST":
        if update_status_form.validate_on_submit():
            return post_update_interview_status(update_status_form, application_id, interview_id, interviewsRepo)
        else:
            flash("Complete all the fields.")
            return display_update_status_form(update_status_form, application_id, interview_id, applicationsRepo, companyRepo)

""" Delete a specific interview: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/delete_interview')
@login_required
def delete_specific_interview(application_id, interview_id):
    return delete_interview(application_id, interview_id, interviewsRepo, interviewPrepRepo, applicationsRepo)

""" View all Interview Preparation: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/view_all_preparation')
@login_required
def view_all_interview_preparation(application_id, interview_id):
    user_id = session["user_id"]
    return display_all_interview_prep_entries(application_id, interview_id, user_id, applicationsRepo, interviewsRepo, interviewPrepRepo, companyRepo)

""" Add Interview Preparation: """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation', methods=["GET", "POST"])
@login_required
def interview_preparation(application_id, interview_id):
    interview_prep_form = AddInterviewPrepForm()
    user_id = session["user_id"]

    if request.method == "POST":
        if interview_prep_form.validate_on_submit():
            return post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, interviewPrepRepo)
        else:
            flash("Complete all the fields.")
            return display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo)

    if request.method == "GET":
        return display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo)

""" View a specific Interview Preparation (entry): """ 
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/view_interview_prep_entry')
@login_required
def view_interview_prep_entry(application_id, interview_id, interview_prep_id):
    return display_interview_prep_details(application_id, interview_id, interview_prep_id, interviewPrepRepo, applicationsRepo, companyRepo, interviewsRepo)

""" Update a specific Interview Preparation (entry): """
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/update_interview_prep_entry', methods=["GET", "POST"])
@login_required
def update_interview_prep(application_id, interview_id, interview_prep_id):
    interview_prep_entry = interviewPrepRepo.getEntryByInterviewPrepID(interview_prep_id)
    update_interview_prep_form = AddInterviewPrepForm(obj=interview_prep_entry)
    
    if request.method == "GET":
        return display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo, interviewsRepo)

    if request.method == "POST":
        if update_interview_prep_form.validate_on_submit():
            return post_update_interview_preparation(application_id, interview_id, interview_prep_id, update_interview_prep_form, interviewPrepRepo)
        else:
            flash("Complete all the fields.")
            return display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo, interviewsRepo)

""" Delete a specific Interview Preparation (entry): """
@app.route('/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/delete_interview_prep_entry', methods=["GET", "POST"])
@login_required
def delete_interview_prep(application_id, interview_id, interview_prep_id):
    return delete_interview_prep_entry(application_id, interview_id, interview_prep_id, interviewPrepRepo)

""" Add a Job Offer: """
@app.route('/applications/<int:application_id>/add_job_offer', methods=["GET", "POST"])
@login_required
def job_offer_form(application_id):
    user_id = session["user_id"]
    add_job_offer = AddJobOffer()
    if request.method == "GET":
        return display_add_job_offer_form(application_id, add_job_offer, companyRepo, applicationsRepo)

    if request.method == "POST":
        if add_job_offer.validate_on_submit():
            return post_add_job_offer(application_id, user_id, add_job_offer, companyRepo, applicationsRepo, jobOffersRepo)
        else: 
            flash("Complete all fields.")
            return display_add_job_offer_form(application_id, add_job_offer, companyRepo, applicationsRepo)

""" View a Job Offer: """
@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>', methods=["GET", "POST"])
@login_required
def view_job_offer_details(application_id, job_offer_id):
    if request.method == "GET":
        return display_job_offer(job_offer_id, jobOffersRepo, companyRepo, applicationsRepo)

""" Update a Job Offer: """
@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>/update_job_offer', methods=["GET", "POST"])
@login_required
def update_job_offer_details(application_id, job_offer_id):
    user_id = session["user_id"]

    job_offer = jobOffersRepo.getJobOfferByID(job_offer_id)
    update_job_offer_form = AddJobOffer(obj=job_offer)

    if request.method == "GET":
        return display_update_job_offer_form(application_id, job_offer_id, update_job_offer_form, jobOffersRepo, companyRepo)

    if request.method == "POST":
        if update_job_offer_form.validate_on_submit():
            return post_update_job_offer(application_id, job_offer_id, update_job_offer_form, jobOffersRepo)

        else: 
            flash("Complete all the fields.")
            return display_update_job_offer_form(application_id, job_offer_id, update_job_offer_form, jobOffersRepo, companyRepo)

""" Delete a Job Offer: """
@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>/delete_job_offer')
@login_required
def delete_job_offer_details(application_id, job_offer_id):
    return delete_job_offer_entry(application_id, job_offer_id, jobOffersRepo)    

""" Display the 'Addressbook' page: """
@app.route('/address_book')
@login_required
def view_address_book():
    """ Display all business contacts to the user """
    user_id = session["user_id"]
    return display_address_book(user_id, companyRepo, contactRepo)

""" View all the 'Contact' entries: """
@app.route('/address_book/contact_list')
@login_required
def view_contact_list():
    user_id = session["user_id"]
    return display_contacts_for_user(user_id, contactRepo)

""" Add a new Contact: """
@app.route('/address_book/contact_list/add_contact', methods=["GET", "POST"])
@login_required
def add_contact():
    user_id = session["user_id"]
    new_contact_form = AddNewContactForm()
    if request.method == "GET":
        return display_add_new_contact_form(new_contact_form)

    if request.method == "POST":
        if new_contact_form.validate_on_submit():
            return post_add_new_contact(new_contact_form, user_id, contactRepo)

        else: 
            flash("Complete all the fields.")
            return display_add_new_contact_form(new_contact_form)

""" View a new Contact: """
@app.route('/address_book/contact_list/<int:contact_id>/view_contact')
@login_required
def view_contact_details(contact_id):
    return display_contact_details(contact_id, contactRepo)

""" Update a new Contact: """
@app.route('/address_book/contact_list/<int:contact_id>/update_contact', methods=["GET", "POST"])
@login_required
def update_contact(contact_id):
    user_id = session["user_id"]
    contact = contactRepo.getContactByID(contact_id)
    update_contact_form = AddNewContactForm(obj=contact)

    if request.method == "GET":
        return display_update_contact_form(contact_id, update_contact_form)

    if request.method == "POST":
        if update_contact_form.validate_on_submit():
            return post_update_contact(contact_id, update_contact_form, contactRepo)

        else: 
            flash("Complete all the fields.")
            return display_update_contact_form(contact_id, update_contact_form)

""" Delete a new Contact: """
@app.route('/address_book/contact_list/<int:contact_id>/delete_contact')
@login_required
def delete_contact(contact_id):
    return delete_contact_details(contact_id, contactRepo)

""" View all the 'Company' entries: """
@app.route('/address_book/company_directory')
@login_required
def display_company_directory():
    user_id = session["user_id"]
    return display_all_companies_for_user(user_id, companyRepo)

""" Add a Company: """
@app.route('/address_book/add_company', methods=["GET", "POST"])
@login_required
def add_company():
    user_id = session["user_id"]
    add_company_form = AddCompanyForm()
    if request.method == "GET":
        return display_add_company_form(add_company_form)

    if request.method == "POST":
        if add_company_form.validate_on_submit():
            return post_add_company(user_id, add_company_form, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_add_company_form(add_company_form)

""" View a Company: """
@app.route('/company/<int:company_id>/view_company', methods=["GET"])
@login_required
def display_company_details(company_id):
    return display_company_profile(company_id, companyRepo)

""" Update a Company: """
@app.route('/company/<int:company_id>/update_company', methods=["GET", "POST"])
@login_required
def update_company_profile(company_id):
    user_id = session["user_id"]
    company_obj = companyRepo.getCompanyById(company_id)
    update_form = UpdateCompany(obj=company_obj)

    if request.method == "GET":
        return display_update_company_profile_form(company_id, update_form, company_obj)

    if request.method == "POST":
        if update_form.validate_on_submit():
            return post_update_company_profile(company_id, user_id, update_form, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_update_company_profile_form(company_id, update_form, company_obj)

""" Delete a Company: """
@app.route('/company/<int:company_id>/delete_company', methods=["GET", "POST"])
@login_required
def delete_company_profile(company_id):
    delete_company_form = DeleteCompanyForm()

    if request.method == "GET":
        return display_delete_company_form(company_id, delete_company_form, companyRepo)

    if request.method == "POST":
        if delete_company_form.validate_on_submit():
            return post_delete_company(company_id, delete_company_form, companyRepo, applicationsRepo, interviewsRepo, interviewPrepRepo, companyNotesRepo, jobOffersRepo, appNotesRepo)
        
        else:
            flash("Complete all the fields.")
            return display_delete_company_form(company_id, delete_company_form, companyRepo)

""" Add a job application (for a specific company): """ 
@app.route('/company/<int:company_id>/add_job_application', methods=["GET", "POST"])
@login_required
def add_company_job_application(company_id):
    user_id = session["user_id"]
    add_job_app_form = AddCompanyJobApplicationForm()
    if request.method == "GET":
        return display_add_company_application_form(add_job_app_form, company_id, companyRepo)

    if request.method == "POST":
        if add_job_app_form.validate_on_submit(): 
            return post_add_company_job_application(user_id, company_id, applicationsRepo, add_job_app_form)
        else: 
            flash("All fields are required.")
            return display_add_company_application_form(add_job_app_form, company_id, companyRepo)

""" View all user notes: """
@app.route('/view_all_notes')
@login_required
def display_all_notes():
    user_id = session["user_id"]
    return display_all_user_notes(user_id, appNotesRepo, companyRepo, applicationsRepo, companyNotesRepo)

""" Add an Application Note for a job application: """
@app.route('/applications/<int:application_id>/app_notes/add_note', methods=["GET", "POST"])
@login_required
def add_application_note(application_id):
    user_id = session["user_id"]
    notes_form = AddApplicationNoteForm() 

    if request.method == "POST":
        if notes_form.validate_on_submit():
            return post_application_add_note(notes_form, application_id, user_id, appNotesRepo, applicationsRepo)
        else:
            flash("All fields are required.")
            return display_application_note_form(notes_form, application_id, companyRepo, applicationsRepo)

    if request.method == "GET":
        return display_application_note_form(notes_form, application_id, companyRepo, applicationsRepo)

""" View all Application Notes: """
@app.route('/applications/<int:application_id>/view_application_notes')
@login_required
def view_application_notes(application_id):
    user_id = session["user_id"]
    return display_application_notes(user_id, application_id, applicationsRepo, appNotesRepo, companyRepo)

""" View (an) Application Note: """
@app.route('/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note')
@login_required
def view_specific_application_note(application_id, app_notes_id):
    return display_application_note_details(application_id, app_notes_id, appNotesRepo, companyRepo)

""" Update an Application Note: """
@app.route('/applications/<int:application_id>/app_notes/<int:app_notes_id>/update_note', methods=["GET", "POST"])
@login_required
def update_user_note(application_id, app_notes_id):
    user_id = session["user_id"]
    app_note_details = appNotesRepo.getNoteByAppNoteID(app_notes_id)
    update_app_note_form = AddApplicationNoteForm(obj=app_note_details)

    if request.method == "POST":
        if update_app_note_form.validate_on_submit():
            return post_update_app_note(update_app_note_form, appNotesRepo, app_notes_id, application_id)
        else:
            flash("All fields are required.")
            return display_update_app_note_form(application_id, user_id, app_notes_id, update_app_note_form, companyRepo, appNotesRepo)

    if request.method == "GET":
        return display_update_app_note_form(application_id, user_id, app_notes_id, update_app_note_form, companyRepo, appNotesRepo)

""" Delete an Application Note: """
@app.route('/applications/<int:application_id>/app_notes/<int:app_notes_id>/delete_note')
@login_required
def delete_an_application_note(application_id, app_notes_id):
    return delete_application_note(application_id, app_notes_id, appNotesRepo)

""" View all notes for a specific company: """
@app.route('/company/<int:company_id>/view_all_company_notes')
@login_required
def display_company_notes(company_id):
    user_id = session["user_id"]
    return display_all_notes_for_a_company(company_id, user_id, companyRepo, companyNotesRepo)

""" Add a Company Note: """
@app.route('/company/<int:company_id>/add_company_note', methods=["GET", "POST"])
@login_required
def add_company_notes(company_id):
    user_id = session["user_id"]
    company_note_form = AddCompanyNoteForm()
    if request.method == "GET":
        return display_add_company_note_form(company_id, company_note_form, companyRepo)

    if request.method == "POST":
        if company_note_form.validate_on_submit():
            return post_add_company_note(user_id, company_id, company_note_form, companyNotesRepo)
        else:
            flash("Complete all the fields.")
            return display_add_company_note_form(company_id, company_note_form, companyRepo)

""" View a Company Note: """
@app.route('/company/<int:company_id>/company_note/<int:company_note_id>/view_note_details')
@login_required
def display_a_specific_note_for_company(company_id, company_note_id):
    user_id = session["user_id"]
    if request.method == "GET":
        return display_company_note_details(company_id, company_note_id, companyRepo, companyNotesRepo)

""" Update a Company Note: """
@app.route('/company/<int:company_id>/company_note/<int:company_note_id>/update_note', methods=["GET", "POST"])
@login_required
def update_company_note(company_id, company_note_id):
    user_id = session["user_id"]
    company_note_obj = companyNotesRepo.getCompanyNoteByID(company_note_id)
    update_note_form = AddCompanyNoteForm(obj=company_note_obj)

    if request.method == "GET":
        return display_update_company_note_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo)
    
    if request.method == "POST":
        if update_note_form.validate_on_submit():
            return post_update_company_form(update_note_form, company_id, company_note_id, companyNotesRepo)
        else: 
            flash("All fields are required.")
            return display_update_company_note_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo)

""" Delete a Company Note: """
@app.route('/company/<int:company_id>/company_note/<int:company_note_id>/delete_note', methods=["GET", "POST"])
@login_required
def delete_company_note(company_id, company_note_id):
    return delete_specific_company_note(company_id, company_note_id, companyNotesRepo)


