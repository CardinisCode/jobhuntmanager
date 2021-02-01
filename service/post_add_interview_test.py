from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def post_add_interview_test(session, user_id, interviewsRepo):

    return redirect("/applications")