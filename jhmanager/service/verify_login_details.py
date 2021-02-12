from flask import Flask, flash, redirect, request, session, render_template
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.hash import sha256_crypt


def verify_login_details(login_form):
    valid_details = False
    username = login_form.username.data
    password = login_form.password.data

    raise ValueError("Details provided:", username, password)

    if not valid_details: 
        flash("Incorrect Username or Password")
        return render_template("login.html")

    flash("Successful login")
    return redirect("/")

