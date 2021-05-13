from flask import Flask, render_template, session, request, redirect, flash


def delete_contact_details(contact_id, contactRepo):
    message = contactRepo.deleteContactByID(contact_id)

    flash(message)
    return redirect('/address_book')