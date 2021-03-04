from jhmanager.repo.database import SqlDatabase
import sqlite3


class InterviewPreparation:
    def __init__(self, db_fields):
        self.prep_id = db_fields[0]
        self.interview_prep_id = db_fields[1]
        self.user_id = db_fields[2]
        self.application_id = db_fields[3]
        self.interview_id = db_fields[4]
        self.question = db_fields[5]
        self.answer = db_fields[6]


class InterviewPreparationRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def addInterviewPrep(self, fields):
        cursor = self.db.cursor()
        command = "INSERT INTO interview_preparation (user_id, application_id, interview_id, specific_question, specific_answer) VALUES (?, ?, ?, ?, ?)"
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid


    def getAllInterviewPrepEntriesByInterviewId(self, interview_id, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interview_preparation WHERE interview_id = {} and user_id = {}".format(interview_id, user_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result: 
            return None

        interview_prep_entries_list = []
        for interview_prep in result: 
            interview_prep_result = InterviewPreparation(interview_prep)
            interview_prep_entries_list.append(interview_prep_result)


        return interview_prep_entries_list

    def deleteByInterviewID(self, interview_prep_id):
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

    def deleteByApplicationID(self, application_id):
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


    def deleteByUserID(self, user_id):
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

    
    