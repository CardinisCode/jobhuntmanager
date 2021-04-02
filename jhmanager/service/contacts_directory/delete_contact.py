from flask import Flask, render_template, session, request, redirect, flash


def delete_contact_details(contact_id, contactRepo):
    message = contactRepo.deleteByContactID(contact_id)

    flash(message)
    return redirect('/address_book')