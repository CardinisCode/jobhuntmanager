from flask import request, render_template, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date
from passlib.hash import sha256_crypt


def post_register_user(session, userRepo, register_form):
    # 1) Extract the data from the form:
    username = register_form.username.data
    email_address = register_form.email_address.data
    hashed_password = sha256_crypt.encrypt((str(register_form.password.data)))

    todays_date = datetime.today()
    str_date = todays_date.strftime('%Y-%m-%d-%X')

    #2) Now to check if username & password already exist in the DB:
    existing_username = userRepo.getByUserName(username)
    if existing_username:
        flash("This username already exists.")
        return render_template("register.html", register_form=register_form)

    existing_email = userRepo.getByUserEmail(email_address)
    if existing_email:
        flash("This email already registered. ")
        return render_template("register.html", register_form=register_form)

    #3) Now that we've checked that this user doesn't already exist, we can safely add their details 
    # as a new a user in our user table:
    registeration_confirmation = userRepo.createUser(username, hashed_password, email_address, str_date)
    session["user_id"] = registeration_confirmation

    flash('Registration Complete!')
    raise ValueError("password is", register_form.password.data, hashed_password)
    return redirect("/")