CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'username' TEXT NOT NULL, 'hash' TEXT NOT NULL, 'email' TEXT NOT NULL);
CREATE UNIQUE INDEX 'user_id' ON "users" ("id");


INSERT INTO users (username, hash, email)
VALUES ('marypoppins1', 'pbkdf2:sha256:150000$USxcihqi$866e1852c8cc6936a41405ebe2825160f2950b8516fdf18c2eaa603b2d54c134', 'marypoppins@gmail.com');

"INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", (username, hashed_password, email))

ALTER TABLE users ADD date datetime;

cursor = self.db.execute("SELECT * FROM users WHERE email=?", (email,))

cursor = self.db.execute("ALTER TABLE company_directory ADD column=? datatype=?", (name, datatype,)) ??? Valid? 
user = cursor.fetchone()

CREATE TABLE IF NOT EXISTS 'company_directory' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'company_name' TEXT NOT NULL);
CREATE UNIQUE INDEX 'company_id' ON "company_directory" ("id");

CREATE TABLE IF NOT EXISTS 'application_history' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'company_name' TEXT NOT NULL, 'date' DATETIME NOT NULL, 'job_role' TEXT NOT NULL, 'platform' TEXT NOT NULL, 'interview_stage' TEXT NOT NULL, 'contact_received' TEXT NOT NULL);
CREATE UNIQUE INDEX 'app_id' ON "application_history" ("id");


