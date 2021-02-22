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

    # def update(self, table, data, company_id, user_id):
    #     columns = ",".join([name for name in data.keys()])
    #     questions = ('?, ' * (len(data.keys()) + 2)).rstrip()[:-1]
    #     values = tuple(data.values())

    #     command = """
    #         UPDATE {} 
    #         SET {} = {}, 
    #             {} = {},
    #             {} = {},
    #             {} = {},
    #             {} = {},
    #             {} = {},
    #         WHERE {} = {} and 'user_id' = {} 
    #     """.format(table, columns, questions, company_id, user_id)
        
    #     cursor = self.db.cursor()
    #     result = cursor.execute(command ,values)
    #     self.db.commit()

    #     return result

    def getByField(self, table, field, value):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM {} WHERE {}={}".format(table, field, value))
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        return data[0]

    def getByID(self, table, field, value):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM {} WHERE {}={}".format(table, field, value))
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        return data


    def getByName(self, table, name, name_value, user_id, userID_value):
        cursor = self.db.cursor()
        command = "SELECT * FROM {} WHERE {} LIKE '{}' and {}={}".format(table, name, name_value, user_id, userID_value)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result]

        if len(data) < 1:
            return None
        
        return data[0]


    """
    TODO
    
    getById
    delete
    query across multiple tables
    update
    """
