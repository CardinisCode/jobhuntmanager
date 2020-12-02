class UserRepository:
    def __init__(self, db):
        self.db = db

    def getById(self, user_id):
        return self.db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)

    def getByUserName(self, username):
        cursor = self.db.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        if not user:
            return None
        return user[0]

    def getByUserEmail(self, email):
        cursor = self.db.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        if not user:
            return None
        return user[0]

    def createUser(self, username, hashed_password, email):
        result = self.db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", (username, hashed_password, email))
        return result.fetchall()
    

    # Possible method to update password hash
    #    def updateCashById(self, user_id, hash):
    #   self.db.execute("UPDATE users SET hash = :hash WHERE id = :user_id", hash=hash, user_id=user_id)