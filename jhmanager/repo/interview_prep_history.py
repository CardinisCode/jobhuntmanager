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


    