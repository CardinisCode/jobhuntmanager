class UserRepository:
    def __init__(self, db):
        self.db = db

    def getById(self, user_id):
        return self.db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)

    def getByUserName(self, username):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        self.db.commit()        

        return result.fetchone()

    def getByUserEmail(self, email):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE email=?", (email,))

        return result.fetchone()

    def getUsernameByUserID(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT username FROM users WHERE id=?", (user_id,))

        return result.fetchone()[0]

    def getEmailAddressByUserID(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT email FROM users WHERE id=?", (user_id,))

        return result.fetchone()[0]

    def createUser(self, username, hashed_password, email, date):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO users (username, hash, email, date) VALUES (?, ?, ?, ?)", (username, hashed_password, email, date,))
        # this was needed. It is a modification to the database and the way that sql works it needs to commit those changes (transaction)
        # which means it saves it to the database. otherwise it forgets the change. This is done to protect the database from corrupting
        # changes
        self.db.commit()

        return result.lastrowid
    

    # Possible method to update password hash
    #    def updateCashById(self, user_id, hash):
    #   self.db.execute("UPDATE users SET hash = :hash WHERE id = :user_id", hash=hash, user_id=user_id)