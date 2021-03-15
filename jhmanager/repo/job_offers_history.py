import sqlite3
from jhmanager.repo.database import SqlDatabase
from flask import flash
from datetime import datetime


class JobOffer:
    date_str = '%Y-%m-%d'
    
    def __init__(self, db_fields):
        self.job_offer_id = db_fields[0]
        self.user_id = db_fields[1]
        self.company_id = db_fields[2]
        self.job_role = db_fields[3]
        self.starting_date = datetime.strptime(db_fields[4], self.date_str)
        self.salary_offered = db_fields[5]
        self.perks_offered = db_fields[6]
        self.offer_response = db_fields[7]


class JobOffersRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def addJobOfferToHistory(self, fields):
        cursor = self.db.cursor()
        command  = """ 
        INSERT INTO job_offers(user_id, company_id, job_role, starting_date, salary_offered, perks_offered, offer_response)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid