from jhmanager.repo.database import SqlDatabase


class InterviewPreparation:
    def __init__(self, db_fields):
        self.interview_prep_id = db_fields[0]
        self.interview_id = db_fields[1]
        self.prep_id = db_fields[2]
        self.question_notes = db_fields[3]


class InterviewPreparationRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    