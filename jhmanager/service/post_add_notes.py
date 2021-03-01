from flask import Flask, render_template, session, request, redirect, flash


def post_add_notes(notes_form, application_id, user_id, userNotesRepo):

    details = {
        "user_id": user_id, 
        "application_id": application_id, 
        "description": notes_form.description.data, 
        "notes_text": notes_form.notes.data
    }

    userNotesRepo.insertNewNotes(details)

    redirect_url = '/applications/{}'.format(application_id)
    flash("Notes successfully saved.")
    return redirect(redirect_url)