from flask import Flask, render_template, session, request, redirect, flash


def delete_application(application_id):
    flash("Application not deleted")
    return redirect('/applications/<int:application_id>')