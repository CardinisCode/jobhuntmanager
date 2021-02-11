from flask import request, render_template, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date


def post_register_user(session, userRepo):
    # username = form.
    # email_address = form.
    # password = form.
    # confirm_password = form.

    # user_details = {}

    raise ValueError("Details captured. Now work on POST")

    # return render_template("userprofile.html")