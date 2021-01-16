class InterviewsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def grabTodaysInterviewCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM interview_history WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result.lastrowid