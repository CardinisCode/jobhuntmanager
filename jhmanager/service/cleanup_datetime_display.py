from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.display_dashboard_content import past_dated_interview


def cleanup_date_format(date_obj): 
    date_str = ""
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    year = date_obj.strftime("%Y")
    month_index = int(date_obj.strftime("%m")) + 1
    month_str = months_list[month_index]
    day_str = date_obj.strftime("%d")
    date_str = day_str + " " + month_str + " " + year

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
