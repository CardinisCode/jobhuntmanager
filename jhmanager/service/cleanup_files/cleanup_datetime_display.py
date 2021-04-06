from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def cleanup_date_format(date_obj): 
    date_str = ""
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    year = date_obj.strftime("%Y")
    month_index = int(date_obj.strftime("%m")) - 1
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


def past_dated(date_obj, time_obj):
    past_dated = False 

    current_date = datetime.now().date()
    current_time = datetime.now().time()

    if date_obj < current_date: 
        past_dated = True
    
    elif date_obj == current_date and time_obj < current_time: 
        past_dated = True

    return past_dated
