from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.display_dashboard_content import past_dated_interview


def cleanup_date_format(date_obj): 
    date_str = ""


    return date_str



def cleanup_time_format(time_obj):
    time_str = ""
    time_format = "%H:%M"

    time_str = time_obj.strftime("%H:%M")
    hour_int = int(time_obj.strftime("%H"))
    if hour_int >= 12:
        time_str += "pm"
    else:
        time_str += "am"

    return time_str
