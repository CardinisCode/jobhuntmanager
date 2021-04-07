from flask import Flask, render_template, session, request, redirect, flash


def replace_na_value_with_none(value): 
    if value == "N/A":
        value = None

    else:
        return value.capitalize()
