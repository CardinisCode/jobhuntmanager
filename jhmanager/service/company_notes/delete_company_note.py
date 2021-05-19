from flask import Flask, render_template, session, request, redirect, flash


def delete_specific_company_note(company_id, company_note_id, companyNotesRepo):
    companyNotesRepo.deleteCompanyNoteByID(company_note_id)

    flash("Note ID #{} has been deleted successfully.".format(company_note_id))
    redirect_url = '/company/{}/view_company'.format(company_id)
    return redirect(redirect_url)