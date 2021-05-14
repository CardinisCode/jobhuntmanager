import sqlite3
from jhmanager.repo.database import DB_LOCATION, SqlDatabase
import pytest


@pytest.fixture(autouse=True)
def before_each():
    db = sqlite3.connect(
        DB_LOCATION,
        detect_types=sqlite3.PARSE_DECLTYPES,
        check_same_thread=False)
    db.execute("DROP TABLE IF EXISTS 'test';")
    db.execute("CREATE TABLE IF NOT EXISTS 'test' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL);")
    db.commit()

class TestDatabase:
    sql = SqlDatabase()
    def test_should_write_to_database(self):
        test_id = self.sql.insert('test', {'name': 'hello'})

        assert test_id == 1

    def test_should_write_multiple_entries_to_db(self):
        test_id = self.sql.insert('test', {'name': 'hello'})
        test_id = self.sql.insert('test', {'name': 'hello'})

        assert test_id == 2
