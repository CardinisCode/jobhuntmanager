import os
import sys

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
# from flask.ext.login import LoginManager

from datetime import datetime, date
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

from jhmanager.helpers_from_cs50_finance import login_required, apology

from jhmanager.repo.users import UserRepository
from jhmanager.repo.company import CompanyRepository
from jhmanager.repo.applications_history import ApplicationsHistoryRepository
from jhmanager.repo.interviewsHistory import InterviewsHistoryRepository

from jhmanager.service.post_registration import post_register_user
from jhmanager.service.homepage import create_homepage_content
from jhmanager.service.post_add_application import post_add_application
from jhmanager.service.display_applications import display_all_applications_current_user
from jhmanager.service.add_interview import grabDetailsFromNewInterviewAndAddToRepo
from jhmanager.service.post_add_interview import post_add_interview
# from jhmanager.service.display_interviews import display_top_10_interviews_to_interviews_html
from jhmanager.service.login import verify_login_details
from jhmanager.service.create_userprofile_content import create_userprofile_content
from jhmanager.service.display_application_details import display_application_details
from jhmanager.service.delete_specific_application import delete_application

from jhmanager.forms.add_interview_form import AddInterviewForm
from jhmanager.forms.add_application_form import AddApplicationForm
from jhmanager.forms.register_form import RegisterUserForm
from jhmanager.forms.login_form import LoginForm


# Configure application
app = Flask(__name__, instance_relative_config=True)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'test_login'

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

@app.route("/register", methods=["GET", "POST"])
def register_user():
    register_form = RegisterUserForm()
    if register_form.validate_on_submit():
        return post_register_user(session, userRepo, register_form)

    """Provide registration form to user"""
    return render_template("register.html", register_form=register_form)


# Taken from CS50's Finance source code & modified

@app.route("/login", methods=["GET", "POST"])
def test_login():
    """Log user in"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return verify_login_details(login_form, userRepo)

    """ Display Login form to the user """
    return render_template("login.html", login_form=login_form)

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/")
@login_required
def index():
    """ Home page for user """
    user_id = session["user_id"]
    return create_homepage_content(session, user_id, applicationsRepo, interviewsRepo, userRepo)

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
@app.route('/applications/<int:application_id>', methods=["GET", "DELETE"])
@login_required
def show_application(application_id):
    # Show the details for a specific application:
    user_id = session["user_id"]
    if request.method == "GET":
        return display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo)

    # elif request.method == "DELETE":
    #     """ Delete a specific application """ 
    #     return delete_application(application_id)

""" Add a new application """
@app.route("/add_job_application", methods=["GET", "POST"])
@login_required
def add_job_application():
    add_application_form = AddApplicationForm()
    user_id = session["user_id"]

    """ Validate the details provided by user & if it passes, display details to user """
    if add_application_form.validate_on_submit():
        return post_add_application(session, user_id, applicationsRepo, companyRepo, add_application_form)

    """ Display Test Add Application form to user """
    return render_template('add_job_application.html', add_application_form=add_application_form)


@app.route('/applications/<int:application_id>/delete_application', methods=["DELETE"])
@login_required
def delete_specific_application(application_id):
    return delete_application(application_id)


# @app.route("/application_details")
# @login_required
# def display_application_details():
#     "Display the application details provided by user"
#     return render_template("application_details.html")


# @app.route("/interviews")
# @login_required
# def display_interviews():
#     """ Display User's Job Interviews """
#     # return render_template("interviews.html")
#     user_id = session["user_id"]
#     return display_top_10_interviews_to_interviews_html(session, user_id, interviewsRepo)


@app.route("/add_interview", methods=["GET", "POST"])
@login_required
def add_interview():
    add_interview_form = AddInterviewForm()
    user_id = session["user_id"]

    """ Validate the details provided by user & if it passes, display details to user """
    if add_interview_form.validate_on_submit(): #POST
        return post_add_interview(session, user_id, add_interview_form, interviewsRepo, applicationsRepo)

    """ Display Add Interview Form to user """ # GET
    return render_template('add_interview.html', add_interview_form=add_interview_form)


@app.route("/interview_details")
@login_required
def display_interview_details():
    """ Display Interview Details to the user """
    return render_template("interview_details.html")


@app.route("/userprofile")
@login_required
def display_user_profile():
    """ Display User Profile """
    user_id = session["user_id"]
    return create_userprofile_content(session, userRepo, user_id)

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


