from flask import Flask, flash, redirect, request, session, render_template
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.hash import sha256_crypt


def verify_login_details(login_form, userRepo):
    username = login_form.username.data
    password = login_form.password.data

    user_exists = userRepo.getByUserName(username)
    if not user_exists:
        flash("Username is not existing.")
        return render_template("login.html", login_form=login_form)

    hashed_password = user_exists[2]
    match = sha256_crypt.verify(password, hashed_password)

    if not match: 
        flash("Incorrect Username or Password")
        return render_template("login.html")

    session["user_id"] = user_exists[0]

    flash("Successful login")
    return redirect("/")
