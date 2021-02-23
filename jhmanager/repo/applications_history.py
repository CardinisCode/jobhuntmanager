import sqlite3
from jhmanager.repo.database import SqlDatabase
from flask import flash


class Application:
    def __init__(self, db_fields):
        self.app_id = db_fields[0]
        self.user_id = db_fields[1]
        self.company_id = db_fields[2]
        self.app_date = db_fields[3]
        self.app_time = db_fields[4]
        self.job_role = db_fields[5]
        self.platform = db_fields[6]
        self.interview_stage = db_fields[7]
        self.employment_type = db_fields[8]
        self.contact_received = db_fields[9]
        self.location = db_fields[10]
        self.job_description = db_fields[11]
        self.user_notes = db_fields[12]
        self.job_perks = db_fields[13]
        self.company_descrip = db_fields[14]
        self.tech_stack = db_fields[15]
        self.job_url = db_fields[16]
        self.job_ref = db_fields[17]
        self.salary = db_fields[18]

    def withCompanyDetails(self, company):
        self.company_name = company.name
        self.company_description = company.description
        self.location = company.location
        self.industry = company.industry

    def __str__(self):
        return ("{} " * 19).format(self.app_id, self.user_id, self.company_id, self.app_date, self.app_time, self.job_role, self.platform, self.interview_stage, self.employment_type, self.contact_received, self.location, self.job_description, self.user_notes, self.job_perks, self.company_descrip, self.tech_stack, self.job_url, self.job_ref, self.salary)


class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def addApplicationToHistory(self, arguments):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO applications (job_role, date, time, employment_type, job_ref, company_descrip, job_description, tech_stack, job_perks, platform, location, salary, user_notes, job_url, user_id, company_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (arguments))
        self.db.commit()

        return result

    def grabTodaysApplicationCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM applications WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result

    def grabTop5ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT date, job_ref, c.name, job_role, platform, employment_type, interview_stage, contact_received, salary FROM applications AS A INNER JOIN company C ON A.company_id = C.company_id WHERE A.user_id = ? ORDER BY date DESC LIMIT 5", (user_id,))
        self.db.commit()

        return result

    def grabTop5ApplicationsByUserID(self, user_id):
        result = self.sql.getByID('applications', 'user_id', user_id)
        # result = self.sql.getByField('applications', 'user_id', user_id)
        applications_list = []

        for application in result:
            application_result = Application(application)
            applications_list.append(application_result)

        return applications_list

    def grabTop10ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT application_id, company_id, date, job_role, employment_type, salary, platform, interview_stage, job_ref, contact_received FROM applications WHERE user_id = ? ORDER BY date DESC LIMIT 10", (user_id,))
        self.db.commit()

        return result


    def grabApplicationDetailsByApplicationID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM applications WHERE application_id = {}".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        return result  

    def deleteEntryByApplicationID(self, application_id):
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM applications WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            print("Application successfully deleted")

        except sqlite3.Error as error:
            print("Application failed to delete.", error)


    def grabApplicationByID(self, application_id):
        result = self.sql.getByField('applications', 'application_id', application_id)

        application_result = Application(result)

        return application_result
      
    def getFullApplicationByApplicationID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT job_role, employment_type, job_ref, c.name, c.description, c.industry, job_description, job_perks, tech_stack, c.location, salary, user_notes, platform, job_url FROM applications as A INNER JOIN company C ON A.company_id = C.company_id WHERE A.application_id = {}".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        data = [d for d in result]

        return data[0] 


    def updateApplicationByID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE applications SET 
            job_role = ?,
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
