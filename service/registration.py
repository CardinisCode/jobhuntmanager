from flask import request, render_template, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology


def valid_username(username, userRepo):
    valid = False


    return valid


def post_registration(session, userRepo, user_id):
    username = request.form.get("username")


    return redirect("/")

