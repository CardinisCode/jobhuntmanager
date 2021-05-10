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
