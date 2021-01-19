import os
import sys

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
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
from service.add_application import grab_users_application_and_add_to_sql_database


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

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
db = sqlite3.connect('jhmanager.db', check_same_thread=False)
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
    return render_template("applications.html")


@app.route("/add_job_application", methods=["GET", "POST"])
@login_required
def add_job_application():
    "Display a form to user that takes input from user"
    if request.method == "GET":
        return render_template("add_job_application.html") 
    
    """ Grab user's input and add it to SQL database for that user """

    return redirect("applications.html")




@app.route("/interviews")
@login_required
def display_interviews():
    """ Display User's Job Interviews """
    return render_template("interviews.html")

@app.route("/add_interview")
@login_required
def add_interview():
    """ Display Form to let user Add an interview """
    return render_template("add_interview.html")

@app.route("/add_job_application")
@login_required
def add_application():
    """ Display Form to let user Add a job Application """
    return render_template("add_job_application.html")

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


