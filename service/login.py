from flask import Flask, flash, redirect, request, session, render_template
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


def validate_user(username, password, userRepo):
    valid = False
    user = None
    if not username: 
        flash('You must provide a username.')
        return (valid, user)

    if not password:
        flash('You must provide a password.')
        return (valid, user)

        # Query database for username
    user_by_username = userRepo.getByUserName(request.form.get("username"))
    user_by_email = userRepo.getByUserEmail(request.form.get("username"))

    # Check username/email matches any user in the database
    if user_by_username == None and user_by_email == None:
        flash("Your username does not match any username/email address that we have.")
        return (valid, user)

    # We have established there is a user which matches the provided username/email address
    # So lets update the user
    user = ""
    if user_by_username != None:
        user = user_by_username
    else:
        user = user_by_email

    # To ensure the password is correct
    if not check_password_hash(user[2], password):
        flash("Incorrect password.")
        return (valid, user)

    return (True, user)


def post_login(session, userRepo):
    # Ensure username was submitted
    username = request.form.get("username")
    password = request.form.get("password")
    valid = validate_user(username, password, userRepo)[0]
    user = validate_user(username, password, userRepo)[1]

    if not valid or not user:
        return render_template("login.html")

    # Remember which user has logged in
    session["user_id"] = user[0]

    # Redirect user to home page
    return redirect("/")
