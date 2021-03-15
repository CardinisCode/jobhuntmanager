
```
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
```


# Checking to see if a value exists in a column of a table using SQLite3:
# Using EXISTS:
```
"SELECT EXISTS(SELECT company_name FROM application_history WHERE company_name LIKE ? and user_id = ?)", (pattern, user_name,)

```

# Updating fields in a table:
```
"UPDATE application_history SET interview_stage = interview_stage WHERE user_id = ? AND company_name LIKE ?", (user_id, company_name,)

UPDATE application_history SET interview_stage = "First interview lined up" WHERE user_id = 2 AND company_name LIKE 'Noir';

```


# Adding a column to an existing table in SQLite3
```
ALTER TABLE users ADD date datetime;
EG: ALTER TABLE application_history ADD "job_url" TEXT NOT NULL DEFAULT "N/A";
```

ALTER TABLE application_history ADD "job_ref" TEXT NOT NULL DEFAULT "N/A";

# Adding values to a table in SQLite3
```
"INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", (username, hashed_password, email))
```

# Grabbing application details for user_id 2:
``` 
"select id, job_role, date from application_history WHERE user_id = 2 ORDER BY id DESC;"

```

# Args for .connect when using SQLite3
```
sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements, uri])

EG: db = sqlite3.connect('jhmanager.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
```

# Deleting a column to recreate it with the correct datatype
# Requires deleting the entire table.
```
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE applications_backup(id, company_name, date, job_role, platform, interview_stage, user_id, employment_type);

INSERT INTO applications_backup SELECT id, company_name, date, job_role, platform, interview_stage, user_id, employment_type FROM application_history;

DROP TABLE application_history;

CREATE TABLE IF NOT EXISTS application_history("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "company_name" TEXT NOT NULL DEFAULT "N/A", "date" DATETIME NOT NULL, "job_role" TEXT NOT NULL DEFAULT "N/A", "platform" TEXT NOT NULL DEFAULT "N/A", "interview_stage" TEXT NOT NULL DEFAULT "N/A", "user_id" INTEGER, "employment_type" TEXT NOT NULL DEFAULT "N/A");

INSERT INTO application_history SELECT id, company_name, date, job_role, platform, interview_stage, user_id, employment_type FROM applications_backup;

DROP TABLE applications_backup;

COMMIT;

```

# Let's re-add the relevant columns as 1 transaction: 
# Note there's no way to add numerous columns at once, so I've instead created a transaction, in which all the alter table commands will be completed.
```
BEGIN TRANSACTION;

ALTER TABLE application_history ADD "contact_received" TEXT NOT NULL DEFAULT "No";
ALTER TABLE application_history ADD "location" TEXT NOT NULL DEFAULT "Remote";
ALTER TABLE application_history ADD "job_description" BLOB NOT NULL DEFAULT "N/A";
ALTER TABLE application_history ADD "user_notes" BLOB NOT NULL DEFAULT "N/A";
ALTER TABLE application_history ADD "job_perks" BLOB NOT NULL DEFAULT "N/A";
ALTER TABLE application_history ADD "company_descrip" BLOB NOT NULL DEFAULT "N/A";
ALTER TABLE application_history ADD "tech_stack" BLOB NOT NULL DEFAULT "N/A";
ALTER TABLE application_history ADD "job_url" BLOB NOT NULL DEFAULT "N/A";

COMMIT;
```


# I want to recreate the application_history with certain fields not being required:

```
BEGIN TRANSACTION;
DROP TABLE application_history;
CREATE TABLE application_history(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "company_name" TEXT NOT NULL, 
    "date" DATETIME NOT NULL, 
    "job_role" TEXT NOT NULL DEFAULT "N/A",
    "platform" TEXT DEFAULT "N/A",
    "interview_stage" TEXT DEFAULT "0",
    "user_id" INTEGER, 
    "employment_type" TEXT DEFAULT "N/A",
    "contact_received" TEXT DEFAULT "No",
    "location" TEXT DEFAULT "Remote",
    "job_description" BLOB DEFAULT "N/A",
    "user_notes" BLOB DEFAULT "N/A",
    "job_perks" BLOB DEFAULT "N/A",
    "company_descrip" BLOB DEFAULT "N/A",
    "tech_stack" BLOB DEFAULT "N/A",
    "job_url" BLOB DEFAULT "N/A",
    "job_ref" TEXT DEFAULT "N/A",
    "salary" TEXT NOT NULL DEFAULT "N/A"
);
COMMIT;
```

```
CREATE TABLE IF NOT EXISTS 'general_preparation' (
    'prep_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id'  INTEGER NOT NULL,
    'question_heading' TEXT DEFAULT "Tell me about yourself",
    'answer_text' BLOB DEFAULT "N/A", 
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
```

```
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
```

```
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
```

```
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
```

```
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE company_backup(company_id, user_id, name, description, location, industry, url, interviewers, contact_number);
INSERT INTO company_backup SELECT company_id, user_id, name, description, location, industry, url, interviewers, contact_number FROM company;
DROP TABLE company;
CREATE TABLE IF NOT EXISTS 'company' (
    'company_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'name' TEXT NOT NULL,
    'description' BLOB DEFAULT "N/A",
    'location' TEXT DEFAULT "N/A",
    'industry' TEXT DEFAULT "N/A",
    'url' TEXT DEFAULT "N/A",
    'interviewers' TEXT DEFAULT "Unknown at present",
    'contact_number' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (user_id) REFERENCES users (user_id)   
);
INSERT INTO company SELECT company_id, user_id, name, description, location, industry, url, interviewers, contact_number FROM company_backup;
DROP TABLE company_backup;
COMMIT;
```

```
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE user_notes_backup(notes_id, user_id, user_id, application_id, company_id, description, notes_text);
INSERT INTO user_notes_backup SELECT notes_id, user_id, user_id, application_id, company_id, description, notes_text FROM user_notes;
DROP TABLE user_notes;
CREATE TABLE IF NOT EXISTS 'user_notes' (
    'notes_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'application_id' INTEGER NOT NULL,
    'company_id' INTEGER NOT NULL, 
    'date' DATETIME NOT NULL,
    'description' TEXT NOT NULL,
    'notes_text' BLOB DEFAULT "N/A",
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (application_id) REFERENCES job_applications (application_id),
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
INSERT INTO user_notes SELECT notes_id, user_id, user_id, application_id, company_id, description, notes_text  FROM user_notes_backup;
DROP TABLE user_notes_backup;
COMMIT;
```

```
ALTER TABLE application_history ADD "interview_time" DATE NOT NULL DEFAULT "HH:MM";
```

```
BEGIN TRANSACTION;
DROP TABLE applications;
CREATE TABLE IF NOT EXISTS applications(
    "application_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "user_id" INTEGER NOT NULL, 
    "company_id" INTEGER NOT NULL, 
    "date" DATETIME NOT NULL, 
    "time" TIME NOT NULL,
    "job_role" TEXT NOT NULL DEFAULT "N/A", 
    "platform" TEXT DEFAULT "N/A", 
    "interview_stage" INTEGER  NOT NULL DEFAULT 0, 
    "employment_type" TEXT DEFAULT "N/A",
    "contact_received" TEXT NOT NULL DEFAULT "No",
    "location" TEXT DEFAULT "Remote",
    "job_description" TEXT DEFAULT "N/A", 
    "user_notes" TEXT DEFAULT "N/A",
    "job_perks" TEXT DEFAULT "N/A",
    "company_descrip" TEXT DEFAULT "N/A",
    "tech_stack" TEXT DEFAULT "N/A",
    "job_url" TEXT DEFAULT "N/A",
    "job_ref" TEXT DEFAULT "N/A",
    "salary" TEXT DEFAULT "N/A", 
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
COMMIT;
```

```
BEGIN TRANSACTION;
DROP TABLE users;
CREATE TABLE IF NOT EXISTS 'users' (
    'user_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'username' TEXT NOT NULL, 
    'hash' TEXT NOT NULL, 
    'email' TEXT NOT NULL, 
    'date' datetime
);
COMMIT;

```
BEGIN TRANSACTION;
DROP TABLE company;
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
```

```
BEGIN TRANSACTION;
DROP TABLE interview_history;
CREATE TABLE IF NOT EXISTS 'interviews' (
    'interview_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'application_id' INTEGER NOT NULL,
    'date' DATETIME NOT NULL, 
    "time" DATETIME NOT NULL,
    "interview_type" TEXT NOT NULL, 
    "interview_location" TEXT DEFAULT "Remote",
    "interview_medium" TEXT,
    "other_medium" TEXT DEFAULT "N/A",
    "contact_number" TEXT DEFAULT "N/A",
    "status" TEXT NOT NULL DEFAULT "upcoming",
    "interviewer_names" TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (application_id) REFERENCES applications (application_id)
);
COMMIT;
```

```
BEGIN TRANSACTION;
DROP TABLE applications;
CREATE TABLE applications(
    "application_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "user_id" INTEGER NOT NULL, 
    "company_id" INTEGER NOT NULL, 
    "date" DATETIME NOT NULL, 
    "time" TIME NOT NULL,
    "job_role" TEXT NOT NULL DEFAULT "N/A", 
    "platform" TEXT DEFAULT "N/A", 
    "interview_stage" INTEGER  NOT NULL DEFAULT 0, 
    "employment_type" TEXT DEFAULT "N/A",
    "contact_received" TEXT NOT NULL DEFAULT "No",
    "location" TEXT DEFAULT "Remote",
    "job_description" BLOB DEFAULT "N/A", 
    "user_notes" BLOB DEFAULT "N/A",
    "job_perks" TEXT DEFAULT "N/A",
    "company_descrip" BLOB DEFAULT "N/A",
    "tech_stack" TEXT DEFAULT "N/A",
    "job_url" BLOB DEFAULT "N/A",
    "job_ref" TEXT DEFAULT "N/A",
    "salary" TEXT DEFAULT "N/A", 
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
COMMIT;
```

BEGIN TRANSACTION;
DROP TABLE interviews;
CREATE TABLE IF NOT EXISTS 'interviews' (
    'interview_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'application_id' INTEGER NOT NULL,
    'date' DATETIME NOT NULL, 
    "time" DATETIME NOT NULL,
    "interview_type" TEXT NOT NULL, 
    "interview_location" TEXT DEFAULT "Remote",
    "interview_medium" TEXT,
    "other_medium" TEXT DEFAULT "N/A",
    "contact_number" TEXT DEFAULT "N/A",
    "status" TEXT NOT NULL DEFAULT "upcoming",
    "interviewer_names" TEXT DEFAULT "Unknown at present", "user_id" INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (application_id) REFERENCES applications (application_id)
);
COMMIT;


# Schema to modify "user_id" field to be a NOT NULL field:
# for 1) application_history
```
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE applications_backup(id, company_name, date, job_role, platform, interview_stage, employment_type, contact_received, location, job_description, user_notes, job_perks, company_descrip, tech_stack, job_url, job_ref, salary, user_id);
INSERT INTO applications_backup SELECT id, company_name, date, job_role, platform, interview_stage, employment_type, contact_received, location, job_description, user_notes, job_perks, company_descrip, tech_stack, job_url, job_ref, salary, user_id FROM application_history;
DROP TABLE application_history;
CREATE TABLE IF NOT EXISTS application_history(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "company_name" TEXT NOT NULL DEFAULT "N/A", 
    "date" DATETIME NOT NULL, 
    "time" TIME NOT NULL,
    "job_role" TEXT NOT NULL DEFAULT "N/A", 
    "platform" TEXT DEFAULT "N/A", 
    "interview_stage" INTEGER  NOT NULL DEFAULT 0, 
    "user_id" INTEGER NOT NULL, 
    "employment_type" TEXT DEFAULT "N/A",
    "contact_received" TEXT NOT NULL DEFAULT "No",
    "location" TEXT DEFAULT "Remote",
    "job_description" TEXT DEFAULT "N/A", 
    "user_notes" TEXT DEFAULT "N/A",
    "job_perks" TEXT DEFAULT "N/A",
    "company_descrip" TEXT DEFAULT "N/A",
    "tech_stack" TEXT DEFAULT "N/A",
    "job_url" TEXT DEFAULT "N/A",
    "job_ref" TEXT DEFAULT "N/A",
    "salary" TEXT DEFAULT "N/A"
);

INSERT INTO application_history SELECT id, company_name, date, job_role, platform, interview_stage, employment_type, contact_received, location, job_description, user_notes, job_perks, company_descrip, tech_stack, job_url, job_ref, salary, user_id FROM applications_backup;
DROP TABLE applications_backup;
COMMIT;

```

# for 2: interview_history:
```
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE interviews_backup(id, company_name, date, time, job_role, user_id, interviewer_names, interview_type, location, interview_medium, other_medium, contact_number, status);
INSERT INTO interviews_backup SELECT id, company_name, date, time, job_role, user_id, interviewer_names, interview_type, location, interview_medium, other_medium, contact_number, status FROM interview_history;
DROP TABLE interview_history;
CREATE TABLE IF NOT EXISTS interview_history(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "company_name" TEXT NOT NULL DEFAULT "N/A",
    "date" DATETIME NOT NULL, 
    "time" DATETIME NOT NULL,
    "job_role" TEXT NOT NULL,
    "user_id" INTEGER NOT NULL, 
    "interviewer_names" TEXT DEFAULT "Unknown at present",
    "interview_type" TEXT NOT NULL, 
    "location" TEXT DEFAULT "Remote",
    "interview_medium" TEXT,
    "other_medium" TEXT DEFAULT "N/A",
    "contact_number" TEXT DEFAULT "N/A",
    "status" TEXT NOT NULL DEFAULT "upcoming"
);
INSERT INTO interview_history SELECT id, company_name, date, time, job_role, user_id, interviewer_names, interview_type, location, interview_medium, other_medium, contact_number, status FROM interviews_backup;
DROP TABLE interviews_backup;
COMMIT;


# Want to modify the fields in interview_history table
# Since there is no data in this table yet, its simpler to drop & recreate the table:
```
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS interviews(
    'interview_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'application_id' INTEGER NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'date' DATETIME NOT NULL, 
    'time' DATETIME NOT NULL,
    'interview_type' TEXT NOT NULL,
    'interview_location' TEXT NOT NULL DEFAULT "Remote",
    'interview_medium' TEXT,
    'other_medium' TEXT DEFAULT "N/A",
    'contact_number' TEXT DEFAULT "N/A",
    'status' TEXT NOT NULL DEFAULT "upcoming",
    'interviewer_names' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (application_id) REFERENCES applications (application_id), 
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
COMMIT;
```


```
BEGIN TRANSACTION;
DROP TABLE interview_preparation;
CREATE TABLE IF NOT EXISTS interview_preparation(
    'interview_prep_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'interview_id' INTEGER NOT NULL, 
    'application_id' INTEGER NOT NULL,
    'user_id' INTEGER NOT NULL,
    'specific_question' TEXT DEFAULT "General Question",
    'specific_answer' BLOB DEFAULT "N/A", 
    FOREIGN KEY (interview_id) REFERENCES interviews (interview_id),
    FOREIGN KEY (application_id) REFERENCES job_applications (application_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
COMMIT;

```


# Updating a SQL query to order by Date and then by time:
``` 
BEGIN TRANSACTION;
SELECT * FROM interview_history
WHERE user_id = 2
ORDER BY
    date DESC, 
    time DESC 
LIMIT 10;
COMMIT;
```

```
BEGIN TRANSACTION;
DROP TABLE interview_preparation;
CREATE TABLE IF NOT EXISTS 'interview_preparation' (
    'interview_prep_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id'  INTEGER NOT NULL,
    'application_id' INTEGER NOT NULL,
    'interview_id' INTEGER NOT NULL,
    'specific_question' TEXT DEFAULT "General Question",
    'specific_answer' BLOB DEFAULT "N/A", 
    FOREIGN KEY (interview_id) REFERENCES interviews (interview_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (application_id) REFERENCES job_applications (application_id)
);
COMMIT;
```



BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS company_notes(
    'company_note_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'date' DATETIME NOT NULL, 
    'subject' TEXT NOT NULL,
    'note_text' BLOB DEFAULT "N/A",
    FOREIGN KEY (user_id) REFERENCES users (user_id)
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
COMMIT;



BEGIN TRANSACTION;
DROP TABLE job_offers;
CREATE TABLE IF NOT EXISTS job_offers(
    'job_offer_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'job_role' TEXT NOT NULL,
    'starting_date' DATETIME NOT NULL, 
    'salary_offered' TEXT NOT NULL,
    'perks_offered' TEXT NOT NULL,
    'offer_response' TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id), 
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);
COMMIT;


