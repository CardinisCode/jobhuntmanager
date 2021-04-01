import os
import sys

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_fontawesome import FontAwesome
from flask_mail import Mail, Message

from datetime import datetime, date
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

from jhmanager.helpers_from_cs50_finance import login_required, apology

from jhmanager.repo.users import UserRepository
from jhmanager.repo.company import CompanyRepository
from jhmanager.repo.applications_history import ApplicationsHistoryRepository
from jhmanager.repo.interviewsHistory import InterviewsHistoryRepository
from jhmanager.repo.general_prep_history import PreparationRepository
from jhmanager.repo.interview_prep_history import InterviewPreparationRepository
from jhmanager.repo.user_notes import UserNotesRepository
from jhmanager.repo.company_notes import CompanyNotesRepository
from jhmanager.repo.job_offers_history import JobOffersRepository
from jhmanager.repo.application_notes import ApplicationNotesRepository
from jhmanager.repo.contacts import ContactRepository

from jhmanager.service.users.register_user import display_register_form
from jhmanager.service.users.register_user import post_register_user
from jhmanager.service.users.user_profile import create_userprofile_content
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
from jhmanager.service.applications.view_all_applications import display_all_applications_current_user

from jhmanager.service.interviews.add_interview import display_add_interview
from jhmanager.service.interviews.add_interview import post_add_interview
from jhmanager.service.interviews.view_interview_details import display_interview_details
from jhmanager.service.interviews.update_interview import display_update_interview_form
from jhmanager.service.interviews.update_interview import post_update_interview
from jhmanager.service.interviews.delete_an_interview import delete_interview
from jhmanager.service.interview_preparation.add_interview_prep import display_interview_preparation_form
from jhmanager.service.interview_preparation.add_interview_prep import post_add_interview_preparation

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
from jhmanager.service.company.delete_company import delete_company_from_db

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
from jhmanager.service.job_offers.delete_job_offer import delete_job_offer_from_db
from jhmanager.service.job_offers.cleanup_job_offer_fields import cleanup_offer_response

from jhmanager.service.display_dashboard_content import create_dashboard_content
from jhmanager.service.display_all_notes import display_all_user_notes
from jhmanager.service.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_datetime_display import cleanup_time_format

from jhmanager.service.address_book.view_address_book import display_address_book

from jhmanager.service.contacts_directory.view_contact_list import display_contacts_for_user

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


# Configure application
app = Flask(__name__, instance_relative_config=True)
mail = Mail()
fa = FontAwesome(app)

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

# # Custom filter
# app.jinja_env.filters["usd"] = usd

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
personalPrepRepo = PreparationRepository(db)
userNotesRepo = UserNotesRepository(db)
companyNotesRepo = CompanyNotesRepository(db)
jobOffersRepo = JobOffersRepository(db)
appNotesRepo = ApplicationNotesRepository(db)
contactRepo = ContactRepository(db)

@app.route("/")
def index():
    """ Landing page that everyone sees """
    return render_template("index.html")


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

@app.route("/login", methods=["GET", "POST"])
def test_login():
    """Log user in"""
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            return post_login(login_form, userRepo)
        else:
            flash("Complete all the fields.")
            return display_login_form(login_form)

    """ Display Login form to the user """
    if request.method == "GET":
        return display_login_form(login_form)

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/dashboard")
@login_required
def display_dashboard():
    user_id = session["user_id"]
    return create_dashboard_content(user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo, jobOffersRepo)


@app.route("/about_us")
def read_about_us():
    return render_template("about_us.html")



"""
CRUD? 
Create -> post
Read -> get
Update -> put
Delete -> delete

GET: /application
    -> all applications
POST: /application
    -> create a single application

GET: /application/{application_id}
        -> view a single application  -> DONE
DELETE: /application/{application_id}
        -> delete this application
PUT: /application/{application_id}
        -> update this application


START HERE
GET: /application/{application_id} 

http://127.0.0.1:5000/application/2

flask example
@app.route('/application/<int:application_id>', methods=["GET"])
def show_application(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
"""

"""
In the case of interview routes:
GET /application/{application_id}/interview/
        -> gets all interviews for an application

GET /application/{application_id}/interview/{interview_id}
        -> gets a specific interview
"""


@app.route("/applications")
@login_required
def display_applications():
    """ Display User's Job Applications """
    user_id = session["user_id"]
    return display_all_applications_current_user(session, user_id, applicationsRepo, companyRepo)

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
    return delete_application(application_id, applicationsRepo, interviewsRepo, interviewPrepRepo, userNotesRepo)


""" Update a Specific application """
@app.route('/applications/<int:application_id>/update_application', methods=["GET", "POST"])
@login_required
def update_specific_application(application_id):
    user_id = session["user_id"]

    application_details = applicationsRepo.grabApplicationByID(application_id)
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


@app.route('/applications/<int:application_id>/add_interview', methods=["GET", "POST"])
@login_required
def add_interview(application_id):
    add_interview_form = AddInterviewForm()
    user_id = session["user_id"]

    # POST
    if request.method == "POST":
        if add_interview_form.validate_on_submit():
            return post_add_interview(session, user_id, add_interview_form, interviewsRepo, applicationsRepo, application_id, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo)

    """ Display add_interview Form to user """
    if request.method == "GET":
        return display_add_interview(add_interview_form, application_id, applicationsRepo, companyRepo)


# View a specific interview:
@app.route('/applications/<int:application_id>/interview/<int:interview_id>')
@login_required
def display_interview(application_id, interview_id):
    """ Display Interview Details for a specific interview to the user """
    user_id = session["user_id"]
    return display_interview_details(session, user_id, interviewsRepo, application_id, interview_id, applicationsRepo, companyRepo)


@app.route('/applications/<int:application_id>/interview/<int:interview_id>/update_interview', methods=["GET", "POST"])
@login_required
def update_specific_interview(application_id, interview_id):
    user_id = session["user_id"]
    interview_details = interviewsRepo.grabInterviewByID(interview_id)
    update_interview_form = AddInterviewForm(obj=interview_details)

    if request.method == "POST":
        if update_interview_form.validate_on_submit():
            return post_update_interview(update_interview_form, user_id, application_id, interview_id, interviewsRepo)
        else:
            flash("Complete all the fields.")
            return display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo)

    if request.method == "GET":
        return display_update_interview_form(update_interview_form, application_id, interview_id, applicationsRepo, companyRepo)


@app.route('/applications/<int:application_id>/interview/<int:interview_id>/delete_interview')
@login_required
def delete_specific_interview(application_id, interview_id):
    return delete_interview(application_id, interview_id, interviewsRepo, interviewPrepRepo, applicationsRepo)


@app.route('/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation', methods=["GET", "POST"])
@login_required
def interview_preparation(application_id, interview_id):
    interview_prep_form = AddInterviewPrepForm()
    user_id = session["user_id"]

    if request.method == "POST":
        if interview_prep_form.validate_on_submit():
            return post_add_interview_preparation(user_id, application_id, interview_id, interview_prep_form, applicationsRepo, interviewPrepRepo)
        else:
            flash("Complete all the fields.")
            return display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo)

    if request.method == "GET":
        return display_interview_preparation_form(user_id, interview_prep_form, application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo)


@app.route('/applications/<int:application_id>/add_job_offer', methods=["GET", "POST"])
@login_required
def job_offer_form(application_id):
    user_id = session["user_id"]
    add_job_offer = AddJobOffer()
    if request.method == "GET":
        return display_add_job_offer_form(application_id, user_id, add_job_offer, companyRepo, applicationsRepo)

    if request.method == "POST":
        if add_job_offer.validate_on_submit():
            return post_add_job_offer(application_id, user_id, add_job_offer, companyRepo, applicationsRepo, jobOffersRepo)
        else: 
            flash("Complete all fields.")
            return display_add_job_offer_form(application_id, user_id, add_job_offer, companyRepo, applicationsRepo)


@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>', methods=["GET", "POST"])
@login_required
def view_job_offer_details(application_id, job_offer_id):
    if request.method == "GET":
        return display_job_offer(job_offer_id, jobOffersRepo, companyRepo, applicationsRepo)


@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>/update_job_offer', methods=["GET", "POST"])
@login_required
def update_job_offer_details(application_id, job_offer_id):
    user_id = session["user_id"]

    job_offer = jobOffersRepo.getJobOfferByJobOfferID(job_offer_id)
    update_job_offer_form = AddJobOffer(obj=job_offer)

    if request.method == "GET":
        return display_update_job_offer_form(application_id, user_id, job_offer_id, update_job_offer_form, job_offer, companyRepo)

    if request.method == "POST":
        if update_job_offer_form.validate_on_submit():
            return post_update_job_offer(application_id, job_offer_id, user_id, update_job_offer_form, jobOffersRepo)

        else: 
            flash("Complete all the fields.")
            return display_update_job_offer_form(application_id, user_id, job_offer_id, update_job_offer_form, job_offer, companyRepo)


@app.route('/applications/<int:application_id>/job_offers/<int:job_offer_id>/delete_job_offer')
@login_required
def delete_job_offer_details(application_id, job_offer_id):
    return delete_job_offer_from_db(application_id, job_offer_id, jobOffersRepo)    


@app.route('/address_book')
@login_required
def view_address_book():
    """ Display all business contacts to the user """
    user_id = session["user_id"]
    return display_address_book(user_id, companyRepo, contactRepo)


@app.route('/address_book/contact_list')
@login_required
def view_contact_list():
    user_id = session["user_id"]
    return display_contacts_for_user(user_id, contactRepo)


@app.route('/address_book/company_directory')
@login_required
def display_company_directory():
    user_id = session["user_id"]
    return display_all_companies_for_user(user_id, companyRepo, applicationsRepo)


@app.route('/address_book/add_company', methods=["GET", "POST"])
@login_required
def add_company():
    user_id = session["user_id"]
    add_company_form = AddCompanyForm()
    if request.method == "GET":
        return display_add_company_form(add_company_form)

    if request.method == "POST":
        if add_company_form.validate_on_submit():
            return post_add_company(user_id, add_company_form, applicationsRepo, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_add_company_form(add_company_form)


@app.route('/company/<int:company_id>/view_company', methods=["GET"])
@login_required
def display_company_details(company_id):
    return display_company_profile(company_id, applicationsRepo, companyRepo)


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
            return post_update_company_profile(company_id, user_id, update_form, company_obj, applicationsRepo, companyRepo)
        else:
            flash("Complete all the fields.")
            return display_update_company_profile_form(company_id, update_form, company_obj)

@app.route('/company/<int:company_id>/delete_company', methods=["GET", "POST"])
@login_required
def delete_company_profile(company_id):
    delete_company_form = DeleteCompanyForm()

    if request.method == "GET":
        return display_delete_company_form(company_id, delete_company_form, companyRepo)

    if request.method == "POST":
        if delete_company_form.validate_on_submit():
            return delete_company_from_db(company_id, delete_company_form, companyRepo, companyNotesRepo, applicationsRepo, interviewsRepo, interviewPrepRepo, userNotesRepo, jobOffersRepo)
        
        else:
            flash("Complete all the fields.")
            return display_delete_company_form(company_id, delete_company_form, companyRepo)


# View all notes for a specific company:
@app.route('/company/<int:company_id>/view_all_company_notes')
@login_required
def display_company_notes(company_id):
    user_id = session["user_id"]
    return display_all_notes_for_a_company(company_id, user_id, companyRepo, companyNotesRepo)


# Add Note for a specific company:
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


# View a specific note for a company:
@app.route('/company/<int:company_id>/company_note/<int:company_note_id>/view_note_details')
@login_required
def display_a_specific_note_for_company(company_id, company_note_id):
    user_id = session["user_id"]
    if request.method == "GET":
        return display_company_note_details(company_id, company_note_id, companyRepo, companyNotesRepo, user_id)


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
            return post_update_company_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo)
        else: 
            flash("All fields are required.")
            return display_update_company_note_form(update_note_form, company_id, company_note_id, companyRepo, companyNotesRepo)


@app.route('/company/<int:company_id>/company_note/<int:company_note_id>/delete_note', methods=["GET", "POST"])
@login_required
def delete_company_note(company_id, company_note_id):
    return delete_specific_company_note(company_id, company_note_id, companyNotesRepo)


# Add a job application for a specific company
@app.route('/company/<int:company_id>/add_job_application', methods=["GET", "POST"])
@login_required
def add_company_job_application(company_id):
    user_id = session["user_id"]
    add_job_app_form = AddCompanyJobApplicationForm()
    if request.method == "GET":
        return display_add_company_application_form(add_job_app_form, company_id, companyRepo)

    if request.method == "POST":
        if add_job_app_form.validate_on_submit(): 
            return post_add_company_job_application(user_id, company_id, applicationsRepo, companyRepo, add_job_app_form)
        else: 
            flash("All fields are required.")
            return display_add_company_application_form(add_job_app_form, company_id, companyRepo)



# Add Note for application:
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


# View all application notes:
@app.route('/applications/<int:application_id>/view_application_notes')
@login_required
def view_application_notes(application_id):
    user_id = session["user_id"]
    return display_application_notes(user_id, application_id, applicationsRepo, appNotesRepo, companyRepo)


# View Details for an Application Note:
@app.route('/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note')
@login_required
def view_specific_application_note(application_id, app_notes_id):
    return display_application_note_details(application_id, app_notes_id, appNotesRepo, companyRepo)


# Update an Application Note:
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


# Delete Note:
@app.route('/applications/<int:application_id>/app_notes/<int:app_notes_id>/delete_note')
@login_required
def delete_an_application_note(application_id, app_notes_id):
    return delete_application_note(application_id, app_notes_id, appNotesRepo)

# View all user notes:
@app.route('/view_all_notes')
@login_required
def display_all_notes():
    user_id = session["user_id"]
    return display_all_user_notes(user_id, appNotesRepo, companyRepo, applicationsRepo, companyNotesRepo)


@app.route("/userprofile")
@login_required
def display_user_profile():
    """ Display User Profile """
    user_id = session["user_id"]
    return create_userprofile_content(session, userRepo, user_id)


@app.route('/userprofile/<int:user_id>/update_email', methods=["GET", "POST"])
@login_required
def update_email_address(user_id):
    user_id = session["user_id"]
    user_details = userRepo.getByUserID(user_id)
    update_email_form = UpdateEmailAddressForm(obj=user_details)

    if request.method == "POST":
        if update_email_form.validate_on_submit():
            return post_update_email_address(update_email_form, userRepo, user_id)
        else:
            flash("All fields are required.")
            return display_update_email_form(user_id, userRepo, update_email_form)

    if request.method == "GET":
        return display_update_email_form(user_id, userRepo, update_email_form)


@app.route('/userprofile/<int:user_id>/change_password', methods=["GET", "POST"])
@login_required
def change_user_password(user_id):
    user_id = session["user_id"]
    change_password_form = ChangePasswordForm()

    if request.method == "POST":
        if change_password_form.validate_on_submit() == False:
            flash("All fields are required.")
            return display_change_password_form(user_id, change_password_form, userRepo)
        if change_password_form.validate_on_submit():
            return post_change_password(user_id, change_password_form, userRepo)

    if request.method == "GET":
        return display_change_password_form(user_id, change_password_form, userRepo)


@app.route('/userprofile/<int:user_id>/delete_account', methods=["GET", "POST"])
@login_required
def delete_user_account(user_id):
    delete_account_form = DeleteAccountForm()

    if request.method == "GET":
        return display_delete_user_form(user_id, delete_account_form)
        
    if request.method == "POST":
        if delete_account_form.validate_on_submit():
            return post_delete_user(delete_account_form, user_id, userRepo, applicationsRepo, userNotesRepo, interviewPrepRepo, interviewsRepo, companyNotesRepo, jobOffersRepo)
        else:
            flash("Failed to delete the account.")
            return display_delete_user_form(user_id, delete_account_form)


@app.route("/calendar")
@login_required
def display_caledar():
    """ Display User's calendar """
    return render_template("calendar.html")

@app.route("/tipsandadvise")
@login_required
def display_tips_and_advise():
    """ Display Tips and Advise to users """
    return render_template("tipsandadvise.html")


