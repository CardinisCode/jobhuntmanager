from flask import Flask, render_template, session, request, redirect


def display_user_note_details(application_id, note_id):
    
    return render_template("view_notes_details.html")