import sqlite3


DB_LOCATION = 'jhmanager/jhmanager.db'

class Database:
    def insert(self, table, data):
        pass

    def getByField(self, table, id):
        pass


class SqlDatabase(Database):
    def __init__(self, db_location=DB_LOCATION, db=None):
        if db == None:
            self.db = sqlite3.connect(
                db_location,
                detect_types=sqlite3.PARSE_DECLTYPES,
                check_same_thread=False)
        else:
            self.db = db

    def insert(self, table, data):
        columns = ",".join([name for name in data.keys()])
        questions = ('?, ' * len(data.keys())).rstrip()[:-1]
        values = tuple(data.values())

        command = "INSERT INTO {} ({}) VALUES ({})".format(table, columns, questions)

        cursor = self.db.cursor()
        result = cursor.execute(command ,values)
        self.db.commit()

        return result.lastrowid

    def getByField(self, table, field, value):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM {} WHERE {}={}".format(table, field, value))
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        return data[0]
