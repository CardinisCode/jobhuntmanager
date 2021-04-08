from flask import Flask, render_template, session, request, redirect


def prepare_company_website_url(company_url): 
    if company_url == "N/A" or company_url == "n/a":
        return None

    elif company_url == "http://" or company_url == "https://":
        return None

    return company_url

