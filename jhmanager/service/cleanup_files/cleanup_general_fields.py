from flask import Flask, render_template, session, request, redirect, flash


def replace_na_value_with_none(value): 
    if value == "N/A":
        value = None

    else:
        return value.capitalize()


def get_count(sql_query):
    count = 0
    if not sql_query:
        return count

    for entry in sql_query:
        count += 1

    return count


def cleanup_field_value(field_value):
    if field_value:
        field_value = (" ".join([x.capitalize() for x in field_value.split(' ')]))
    return field_value


def cleanup_urls(url):
    if url == "N/A" or url == "n/a":
        return None

    elif url == "http://" or url == "https://":
        return None

    return url