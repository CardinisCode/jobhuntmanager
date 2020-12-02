class UserRepository:
    def __init__(self, db):
        self.db = db

    def getById(self, user_id):
        return self.db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)

    def getByUserName(self, username):
        user = self.db.execute(
            "SELECT * FROM users WHERE username = :username",
            username=username
            )
        if len(user) == 0:
            return None
        return user[0]

    def getByUserEmail(self, email):
        user = self.db.execute(
            "SELECT * FROM users WHERE email = :email",
            email=email
        )
        if len(user) == 0:
            return None
        return user[0]

    def createUser(self, username, hashed_password, email):
        return self.db.execute("INSERT INTO users (username, hash, email) VALUES (:username, :hash, :email)", username=username, hash=hashed_password, email=email)

    # Possible method to update password hash
    #    def updateCashById(self, user_id, hash):
    #   self.db.execute("UPDATE users SET hash = :hash WHERE id = :user_id", hash=hash, user_id=user_id)