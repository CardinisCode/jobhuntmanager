from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def post_update_user_note(update_note_form, userNotesRepo, note_id, application_id):
    details = {
        "description": update_note_form.description.data, 
        "notes_text": update_note_form.user_notes.data,
        "note_id": note_id
    }

    message = userNotesRepo.updateByID(details)


    redirect_url = '/applications/{}/view_notes'.format(application_id)
    flash(message)
    return redirect(redirect_url)
