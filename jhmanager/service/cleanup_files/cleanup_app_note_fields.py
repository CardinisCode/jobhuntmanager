from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, date
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format


def cleanup_app_notes(app_notes_details, entry_id):
    entry_date = app_notes_details["fields"][entry_id]["entry_date"]
    date_obj = datetime.strptime(entry_date, "%Y-%m-%d")
    app_notes_details["fields"][entry_id]["entry_date"] = cleanup_date_format(date_obj)