from flask import Flask, flash, redirect, request, session, render_template
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.hash import sha256_crypt


def validate_user(username, password, userRepo):
    valid = False
    user = None

    # Query database for username
    user_by_username = userRepo.getByUserName(request.form.get("username"))
    user_by_email = userRepo.getByUserEmail(request.form.get("username"))

    # Check username/email matches any user in the database
    if user_by_username:
        user_password = user_by_username[2]
    if user_by_email: 
        user_password = user_by_email[2]

    # # We have established there is a user which matches the provided username/email address
    # So lets update the user
    user = ""
    if user_by_username:
        user = user_by_username
    else:
        user = user_by_email 

    # To ensure the password is correct
    # We will hash the provided password & see if it matches the password on file:
    hashed_password = sha256_crypt.encrypt(str(password))
    match = sha256_crypt.verify(hashed_password, user_password)
    # raise ValueError("PW On file:", user_password, "vs provided pw:", hashed_password, match)

    if not match:
        flash("Incorrect password.")
        return (valid, user)

    return (True, user)


def post_login(session, userRepo):
#     # Ensure username was submitted
    username = request.form.get("username")
    password = request.form.get("password")
    valid = validate_user(username, password, userRepo)[0]
    user = validate_user(username, password, userRepo)[1]

    if not valid or not user:
        return render_template("login.html")

    # Remember which user has logged in
    session["user_id"] = user[0]

#     # Redirect user to home page
    return redirect("/")
