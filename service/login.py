from flask import Flask, flash, redirect, request, session
from flask_session import Session

def post_login(session, userRepo):
    # Ensure email was submitted
        if not request.form.get("email"):
            return apology("must provide email address", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        user = userRepo.getByUserName(request.form.get("email"))

        # Ensure username exists and password is correct
        if user is None or not check_password_hash(user["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user["id"]

        # Redirect user to home page
        return redirect("/")
