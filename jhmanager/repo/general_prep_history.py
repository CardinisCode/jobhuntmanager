from jhmanager.repo.database import SqlDatabase
import sqlite3

class Preparation:
    def __init__(self, db_fields):
        self.prep_id = db_fields[0]
        self.user_id= db_fields[1]
        self.question = db_fields[2]
        self.answer_text = db_fields[3]

    
class PreparationRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def deleteByPrepID(self, prep_id): 
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM general_preparation WHERE prep_id = {}".format(prep_id)
            cursor.execute(command)
            self.db.commit()
            message = "Preparation entry deleted successfully."

        except sqlite3.Error as error:
            message = "Preparation entry failed to delete. " + error
        finally:
            return message

    def deleteByUserID(self, user_id): 
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM general_preparation WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Preparation entry deleted successfully."

        except sqlite3.Error as error:
            message = "Preparation entry failed to delete. " + error
        finally:
            return message    