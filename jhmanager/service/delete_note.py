from flask import Flask, render_template, session, request, redirect, flash


def delete_note_for_application(application_id, note_id, userNotesRepo):
    message = userNotesRepo.deleteByNoteID(note_id)
    redirect_url = '/applications/{}/view_notes'.format(application_id)
    flash(message)
    return redirect(redirect_url)