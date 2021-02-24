from jhmanager.repo.database import SqlDatabase

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