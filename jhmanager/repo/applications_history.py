import sqlite3
from jhmanager.repo.database import SqlDatabase
from flask import flash
from datetime import datetime


class Application:
    date_str = '%Y-%m-%d'
    
    def __init__(self, db_fields):
        self.app_id = db_fields[0]
        self.user_id = db_fields[1]
        self.company_id = db_fields[2]
        self.app_date = db_fields[3]
        self.app_time = db_fields[4]
        self.date_posted = datetime.strptime(db_fields[5], self.date_str)
        self.job_role = db_fields[6]
        self.platform = db_fields[7]
        self.interview_stage = db_fields[8]
        self.employment_type = db_fields[9]
        self.contact_received = db_fields[10]
        self.location = db_fields[11]
        self.job_description = db_fields[12]
        self.user_notes = db_fields[13]
        self.job_perks = db_fields[14]
        self.tech_stack = db_fields[15]
        self.job_url = db_fields[16]
        self.job_ref = db_fields[17]
        self.salary = db_fields[18]

    def withCompanyDetails(self, company):
        self.company_name = company.name
        self.company_description = company.description
        self.company_location = company.location
        self.industry = company.industry

    def __str__(self):
        return ("{} " * 19).format(self.app_id, self.user_id, self.company_id, self.app_date, self.app_time, self.date_posted, self.job_role, self.platform, self.interview_stage, self.employment_type, self.contact_received, self.location, self.job_description, self.user_notes, self.job_perks, self.tech_stack, self.job_url, self.job_ref, self.salary)


class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def addApplicationToHistory(self, fields):
        cursor = self.db.cursor()
        command = """ 
            INSERT INTO job_applications
                (user_id, company_id, app_date, app_time, date_posted, job_role, platform, employment_type, job_description, user_notes, job_perks, tech_stack, job_url, job_ref, salary)
            VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """ 
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid

    def grabTop10ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM job_applications WHERE user_id = ? ORDER BY application_id DESC LIMIT 10", (user_id,))
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if len(data) < 1:
            return None

        applications_list = []

        for application in data:
            application_result = Application(application)
            applications_list.append(application_result)

        return applications_list
 

    def getAllApplicationsByUserID(self, user_id):
        cursor = self.db.cursor()
        command = """  
            SELECT * FROM job_applications
            WHERE user_id = {}
        """.format(user_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if not result: 
            return None

        applications_list = []

        for application in data:
            application_result = Application(application)
            applications_list.append(application_result)

        return applications_list

    def grabApplicationByID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM job_applications WHERE application_id = {}".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if not data:
            return None

        application = Application(data[0])
        
        return application  

    
    def getApplicationsByCompanyID(self, company_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM job_applications WHERE company_id = {}".format(company_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if not data:
            return None

        application_list = []
        for application in data:
            application_result = Application(application)
            application_list.append(application_result)
        
        return application_list  
 

    def updateInterviewStage(self, fields):
        try: 
            cursor = self.db.cursor()
            command = """
            UPDATE job_applications
            SET interview_stage = ?
            WHERE application_id = ?"""
            cursor.execute(command, tuple(fields.values()))
            self.db.commit()
            message = "Interview Stage for this application has been updated!"

        except sqlite3.Error as error:
            message = "Interview Stage failed to update. " + error
        finally:
            return message


    def updateApplicationByID(self, fields):
        cursor = self.db.cursor()
        
        command = """
            UPDATE job_applications 
            SET job_role = ?,
                employment_type = ?,
                job_ref = ?,
                job_description = ?,
                job_perks = ?,
                tech_stack = ?,
                salary = ?,
                user_notes = ?,
                platform = ?,
                job_url = ?
            WHERE application_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()
        

    def deleteApplicationByID(self, application_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_applications WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            message = "Application successfully deleted"

        except sqlite3.Error as error:
            message = "Application failed to delete. " + error
        finally:
            return message 

    def deleteApplicationsByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_applications WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Application successfully deleted"

        except sqlite3.Error as error:
            message = "Application failed to delete. " + error
        finally:
            return message 

    def deleteApplicationByCompanyID(self, company_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM job_applications WHERE company_id = {}".format(company_id)
            cursor.execute(command)
            self.db.commit()
            message = "Application successfully deleted"

        except sqlite3.Error as error:
            message = "Application failed to delete. " + error
        finally:
            return message 