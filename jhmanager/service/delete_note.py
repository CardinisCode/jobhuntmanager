from flask import Flask, render_template, session, request, redirect, flash


def delete_note_for_application(application_id, note_id, userNotesRepo):
    
    redirect_url = '/applications/{}/view_notes'.format(application_id)
    flash("Note Successfully deleted.")
    return redirect(redirect_url)