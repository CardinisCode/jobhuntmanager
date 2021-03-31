import sqlite3
from jhmanager.repo.database import SqlDatabase
from flask import flash
from datetime import datetime


class JobOffer:
    date_str = '%Y-%m-%d'
    
    def __init__(self, db_fields):
        # raise  ValueError(db_fields)
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

    def getJobOfferByJobOfferID(self, job_offer_id):
        cursor = self.db.cursor()
        command = """ 
            SELECT * FROM job_offers
            where job_offer_id = {}
        """.format(job_offer_id)
        
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if len(data) < 1:
            return None

        job_offer = JobOffer(data[0])

        return job_offer


    def getJobOffersByUserId(self, user_id):
        cursor = self.db.cursor()
        command = """ 
            SELECT * FROM job_offers
            where user_id = {}
            ORDER BY starting_date DESC
        """.format(user_id)
        
        result = cursor.execute(command)
        self.db.commit()

        offers_list = []

        for offer in result:
            job_offer_result = JobOffer(offer)
            offers_list.append(job_offer_result)

        if offers_list == []:
            return None

        return offers_list
       

    def updateByJobOfferID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE job_offers 
        SET job_role = ?,
            starting_date = ?,
            salary_offered = ?, 
            perks_offered = ?,
            offer_response = ?
        WHERE job_offer_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()
    

    def deleteByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_offers WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Job offer successfully deleted"

        except sqlite3.Error as error:
            message = "Failed to delete all Job offers for this user. " + error
        finally:
            return message 

    def deleteByCompanyID(self, company_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_offers WHERE company_id = {}".format(company_id)
            cursor.execute(command)
            self.db.commit()
            message = "Job offer successfully deleted"

        except sqlite3.Error as error:
            message = "Failed to delete all Job offers for this company. " + error
        finally:
            return message 

    def deleteByJobOfferID(self, job_offer_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_offers WHERE job_offer_id = {}".format(job_offer_id)
            cursor.execute(command)
            self.db.commit()
            message = "Job offer successfully deleted"

        except sqlite3.Error as error:
            message = "Failed to delete all Job offers for this user. " + error
        finally:
            return message 