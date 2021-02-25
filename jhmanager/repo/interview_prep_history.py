from jhmanager.repo.database import SqlDatabase


class InterviewPreparation:
    def __init__(self, db_fields):
        self.interview_prep_id = db_fields[0]
        self.interview_id = db_fields[1]
        self.prep_id = db_fields[2]
        self.question = db_fields[3]
        self.answer = db_fields[4]


class InterviewPreparationRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def addInterviewPrep(self, fields):
        cursor = self.db.cursor()
        command = "INSERT INTO interview_preparation (user_id, interview_id, specific_question, specific_answer) VALUES (?, ?, ?, ?)"
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid