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

CREATE TABLE IF NOT EXISTS 'interview_history' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'company_name' TEXT NOT NULL, 'date' DATETIME NOT NULL, 'time' DATETIME NOT NULL,'job_role' TEXT NOT NULL, 'interview_stage' TEXT NOT NULL, 'user_id' INTEGER NOT NULL, 'status' TEXT NOT NULL);
CREATE UNIQUE INDEX 'interview_id' ON "interview_history" ("id");


CREATE TABLE IF NOT EXISTS 'general_preparation' (
    'prep_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id'  INTEGER NOT NULL,
    'question_heading' TEXT DEFAULT "Tell me about yourself",
    'answer_text' BLOB DEFAULT "N/A", 
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE IF NOT EXISTS 'interview_preparation' (
    'interview_prep_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'prep_id' INTEGER NOT NULL,
    'user_id'  INTEGER NOT NULL,
    'interview_id' INTEGER NOT NULL,
    'specific_question' TEXT DEFAULT "General Question",
    'specific_answer' BLOB DEFAULT "N/A", 
    FOREIGN KEY (prep_id) REFERENCES general_preparation (prep_id),
    FOREIGN KEY (interview_id) REFERENCES interviews (interview_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);


BEGIN TRANSACTION;
DROP TABLE job_applications;
CREATE TABLE job_applications(
    'application_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'date' DATETIME NOT NULL, 
    'time' TIME NOT NULL,
    'date_posted' DATETIME NOT NULL,
    'job_role' TEXT NOT NULL DEFAULT "N/A", 
    'platform' TEXT DEFAULT "N/A", 
    'interview_stage' INTEGER  NOT NULL DEFAULT 0, 
    'employment_type' TEXT DEFAULT "N/A",
    'contact_received' TEXT NOT NULL DEFAULT "No",
    'location' TEXT DEFAULT "Remote",
    'job_description' BLOB DEFAULT "N/A", 
    'user_notes' BLOB DEFAULT "N/A",
    'job_perks' TEXT DEFAULT "N/A",
    'tech_stack' TEXT DEFAULT "N/A",
    'job_url' BLOB DEFAULT "N/A",
    'job_ref' TEXT DEFAULT "N/A",
    'salary' TEXT DEFAULT "N/A", 
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
COMMIT;


BEGIN TRANSACTION;
DROP TABLE job_applications;
CREATE TABLE IF NOT EXISTS 'company' (
    'company_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'name' TEXT NOT NULL,
    'description' TEXT DEFAULT "N/A",
    'location' TEXT DEFAULT "N/A",
    'industry' TEXT DEFAULT "N/A",
    'url' TEXT DEFAULT "N/A",
    'interviewers' TEXT DEFAULT "Unknown at present",
    'contact_number' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (user_id) REFERENCES users (user_id)   
);
COMMIT;