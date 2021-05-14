from jhmanager.repo.database import SqlDatabase
import sqlite3



class Company:
    def __init__(self, db_fields):
        self.company_id = db_fields[0]
        self.user_id = db_fields[1]
        self.name = db_fields[2]
        self.description = db_fields[3]
        self.location = db_fields[4]
        self.industry = db_fields[5]
        self.url = db_fields[6]
        self.interviewers = db_fields[7]
        self.contact_number = db_fields[8]

    
class CompanyRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def createCompany(self, fields):
        cursor = self.db.cursor()
        command = """
        INSERT INTO company 
        (user_id, name, description, location, industry, url, interviewers, contact_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid

    def getCompanyById(self, company_id):
        result = self.sql.getByField('company', 'company_id', company_id)

        company = Company(result)

        return company

    def getCompanyByName(self, company_name, user_id) -> Company:
        result = self.sql.getByName('company', 'name', company_name, 'user_id', user_id)

        if not result:
            return None

        company = Company(result)

        return company

    def getCompanyEntriesByUserID(self, user_id):
        cursor = self.db.cursor()
        command = """  
        SELECT * FROM company
        WHERE user_id = {}
        ORDER BY name
        """.format(user_id)

        result = cursor.execute(command)
        self.db.commit()

        company_list = []

        if not result: 
            return None

        for company in result:
            company_result = Company(company)
            company_list.append(company_result)

        return company_list

    def getTop8CompaniesByUserID(self, user_id):
        cursor = self.db.cursor()
        command = """  
        SELECT * FROM company
        WHERE user_id = {}
        ORDER BY name
        LIMIT 8
        """.format(user_id)

        result = cursor.execute(command)
        self.db.commit()

        company_list = []

        if not result: 
            return None

        for company in result:
            company_result = Company(company)
            company_list.append(company_result)

        return company_list

    def updateCompanyByID(self, fields):
        cursor = self.db.cursor()
        command = """
        UPDATE company 
        SET name = ?,
            description = ?,
            industry = ?,
            location = ?, 
            url = ?, 
            interviewers = ?,
            contact_number = ?
        WHERE user_id = ? and company_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    # This method updates a company entry using details received from a job application. 
    def updateCompanyByApplication(self, fields):
        cursor = self.db.cursor()
        command = """
        UPDATE company 
        SET name = ?,
            description = ?,
            industry = ?,
            location = ?, 
        WHERE user_id = ? and company_id = ?"""

        cursor.execute(command, tuple(fields.values()))
        self.db.commit()


    def deleteCompanyByID(self, company_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM company WHERE company_id = {}".format(company_id)
            cursor.execute(command)
            self.db.commit()
            message = "Company deleted successfully."

        except sqlite3.Error as error:
            message = "Company failed to delete. " + error
        finally:
            return message

    def deleteAllCompaniesByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM company WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Company deleted successfully."

        except sqlite3.Error as error:
            message = "Company failed to delete. " + error
        finally:
            return message


    