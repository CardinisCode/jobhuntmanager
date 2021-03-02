from flask import Flask, render_template, session, request, redirect


def display_all_user_notes(user_id):
    
    return render_template("view_all_user_notes.html")