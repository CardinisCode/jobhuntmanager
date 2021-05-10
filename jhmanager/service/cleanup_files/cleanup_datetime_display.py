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


def verify_value_is_date_obj(date_value):
    value_obj = None
    if type(date_value) == 'str':
        value_obj = datetime.strptime(date_value, "%Y-%m-%d")
    else:
        value_obj = date_value
    return value_obj


def verify_value_is_time_obj(time_value):
    value_obj = None
    if type(time_value) == 'str':
        value_obj = datetime.strptime(time_value, "%H:%M")
    else:
        value_obj = time_value
    return value_obj


def past_dated(date_obj, time_obj):
    updated_date_obj = verify_value_is_date_obj(date_obj)
    updated_time_obj = verify_value_is_time_obj(time_obj)
    date_is_past_dated = False 

    current_date = datetime.now().date()
    current_time = datetime.now().time()

    if type(updated_date_obj) == type(current_date) and updated_date_obj < current_date: 
        date_is_past_dated = True
    
    elif updated_date_obj == current_date and updated_time_obj < current_time: 
        date_is_past_dated = True

    return date_is_past_dated


def present_dated(date_obj):
    current_date = datetime.now().date()
    date_is_today = False 

    if date_obj == current_date: 
        date_is_today = True
        
    return date_is_today