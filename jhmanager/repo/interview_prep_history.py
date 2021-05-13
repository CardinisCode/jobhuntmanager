from jhmanager.repo.database import SqlDatabase
import sqlite3


class InterviewPreparation:
    def __init__(self, db_fields):
        self.interview_prep_id = db_fields[0]
        self.interview_id = db_fields[1]
        self.application_id = db_fields[2]
        self.user_id = db_fields[3]
        self.question = db_fields[4]
        self.answer = db_fields[5]


class InterviewPreparationRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def createInterviewPreparation(self, fields):
        cursor = self.db.cursor()
        command = "INSERT INTO interview_preparation (user_id, application_id, interview_id, specific_question, specific_answer) VALUES (?, ?, ?, ?, ?)"
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid

    def getInterviewPrepByID(self, interview_prep_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interview_preparation WHERE interview_prep_id = {}".format(interview_prep_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]
        if not data:
            return None

        interview_prep_entry = InterviewPreparation(data[0])
        
        return interview_prep_entry  

    def getAllInterviewPrepEntriesByInterviewId(self, interview_id, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interview_preparation WHERE interview_id = {} and user_id = {} ORDER BY specific_question".format(interview_id, user_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result: 
            return None

        interview_prep_entries_list = []
        for interview_prep in result: 
            
            interview_prep_result = InterviewPreparation(interview_prep)
            interview_prep_entries_list.append(interview_prep_result)

        return interview_prep_entries_list

    def updateInterviewPrepByID(self, fields):
        output = None
        try: 
            cursor = self.db.cursor()
            command = """
            UPDATE interview_preparation
            SET specific_question = ?,
                specific_answer = ?
            WHERE interview_prep_id = ?"""
            cursor.execute(command, tuple(fields.values()))
            self.db.commit()
            output = True

        except:
            output = False
        finally:
            return output
    

    def deleteInterviewPrepByID(self, interview_prep_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interview_preparation WHERE interview_prep_id = {}".format(interview_prep_id)
            cursor.execute(command)
            self.db.commit()
            message = "Details for Interview Preparation deleted successfully."

        except sqlite3.Error as error:
            message = "Details for Interview Preparation failed to delete. " + error
        finally:
            return message

    def deleteInterviewPrepByInterviewID(self, interview_prep_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interview_preparation WHERE interview_prep_id = {}".format(interview_prep_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interview Preparation entry deleted successfully."

        except sqlite3.Error as error:
            message = "Interview Preparation entry failed to delete. " + error
        finally:
            return message

    def deleteInterviewPrepByApplicationID(self, application_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interview_preparation WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interview Preparation entries deleted successfully."

        except sqlite3.Error as error:
            message = "Interview Preparation entries failed to delete. " + error
        finally:
            return message

    def deleteInterviewPrepByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interview_preparation WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interview Preparation entries deleted successfully."

        except sqlite3.Error as error:
            message = "Interview Preparation entries failed to delete. " + error
        finally:
            return message

    
    