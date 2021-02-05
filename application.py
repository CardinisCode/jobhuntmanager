import os
import sys

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

from datetime import datetime, date
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp

from helpers_from_cs50_finance import login_required, apology

from repo.users import UserRepository
from repo.company_directory import CompanyRepository
from repo.applications_history import ApplicationsHistoryRepository
from repo.interviewsHistory import InterviewsHistoryRepository

from service.registration import post_registration
from service.homepage import create_homepage_content
from service.login import post_login
from service.post_add_application import post_add_application
from service.display_applications import display_all_applications_current_user
from service.add_interview import grabDetailsFromNewInterviewAndAddToRepo
from service.post_add_interview import post_add_interview
from service.display_interviews import display_top_10_interviews_to_interviews_html

from forms import AddInterviewForm
from forms import AddApplicationForm


# Configure application
app = Flask(__name__)
Bootstrap(app)
datepicker(app)

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
db = sqlite3.connect('jhmanager.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
userRepo = UserRepository(db)
companyRepo = CompanyRepository(db)
applicationsRepo = ApplicationsHistoryRepository(db)
interviewsRepo = InterviewsHistoryRepository(db)

@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Provide registration form to user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        return post_registration(session, userRepo)


# Taken from CS50's Finance source code & modified

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # user_id = session["user_id"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return post_login(session, userRepo)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


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
    return create_homepage_content(session, user_id, applicationsRepo, interviewsRepo)


@app.route("/applications")
@login_required
def display_applications():
    """ Display User's Job Applications """
    user_id = session["user_id"]
    return display_all_applications_current_user(session, user_id, applicationsRepo)


@app.route("/add_job_application", methods=["GET", "POST"])
@login_required
def add_job_application():
    add_application_form = AddApplicationForm()
    user_id = session["user_id"]

    """ Validate the details provided by user & if it passes, display details to user """
    if add_application_form.validate_on_submit():
        return post_add_application(session, user_id, applicationsRepo, add_application_form)

    """ Display Test Add Application form to user """
    return render_template('add_job_application.html', add_application_form=add_application_form)


@app.route("/application_details")
@login_required
def display_application_details():
    "Display the application details provided by user"
    return render_template("application_details.html")


@app.route("/interviews")
@login_required
def display_interviews():
    """ Display User's Job Interviews """
    # return render_template("interviews.html")
    user_id = session["user_id"]
    return display_top_10_interviews_to_interviews_html(session, user_id, interviewsRepo)


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
    return render_template("userprofile.html")

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


