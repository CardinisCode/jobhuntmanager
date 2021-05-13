from flask import Flask, render_template, session, request, redirect, flash


def delete_application_note(application_id, app_notes_id, appNotesRepo):
    message = appNotesRepo.deleteNoteByAppNoteID(app_notes_id)
    redirect_url = '/applications/{}/view_application_notes'.format(application_id)
    flash(message)
    return redirect(redirect_url)