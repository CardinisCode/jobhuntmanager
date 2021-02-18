This Should detail what your project is about and what problem your program will solve

## Getting Started

Setup environment variables, in the terminal copy and enter these lines of code:
(**** You'll need to do this every time you close and reopen this project. ***)

```
export FLASK_ENV=development                      
export FLASK_DEBUG=1                              
export FLASK_APP=application.py 
```

Run Flask server:

```
flask run
```


# Using a form to create a button 

```
<form action="https://google.com">
    <input type="submit" value="Go to Google" />
</form>
```

# Using an 'a' (anchor) reference and just style it to look like a button

```
<a href="https://google.com" class="button">Go to Google</a>
```

# Setting up a link to another page on your website:
```
<a href="/html_file_name">Page Name</a>
EG: <a href="/add_job_application" class="button left_button">Add Application</a>
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

## FLASK:

# WTForms:
# Going to use WTForms to assist me in creating forms
# Since it allows me to pre-populate fields as well. 

# To use this, install the relevant library:
```
pip3 install flask-wtf
```

# To access Flask's Datepicker
# For Python3:
```
pip3 install Flask-Datepicker
```

# Inside Flask App, Add:
```
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

app = Flask(__name__)
Bootstrap(app)
datepicker(app)
```

# Want to modify the fields in interview_history table
# Since there is no data in this table yet, its simpler to drop & recreate the table:
```
BEGIN TRANSACTION;
DROP TABLE interview_history;
CREATE TABLE IF NOT EXISTS interview_history(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "company_name" TEXT NOT NULL DEFAULT "N/A", 
    "date" DATETIME NOT NULL, 
    "time" DATETIME NOT NULL,
    "job_role" TEXT NOT NULL DEFAULT "N/A", 
    "interviewer_names" TEXT NOT NULL DEFAULT "N/A", 
    "user_id" INTEGER,
    "interview_type" TEXT NOT NULL, 
    "interview_location" TEXT NOT NULL DEFAULT "Remote",
    "interview_medium" TEXT NOT NULL,
    "other_medium" TEXT NOT NULL DEFAULT "N/A",
    "contact_number" TEXT NOT NULL DEFAULT "N/A"
);
CREATE UNIQUE INDEX 'interview_id' ON "interview_history" ("id");
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

```

# To check whether your current version of SQLite supports foreign key constraints or not, you use the following command.
```
PRAGMA foreign_keys;
```

# The command returns an integer value: 1: enable, 0: disabled. If the command returns nothing, it means that your SQLite version doesn’t support foreign key constraints.

# To disable foreign key constraint:
```
PRAGMA foreign_keys = OFF;
```

# To enable foreign key constraint:
```
PRAGMA foreign_keys = ON;
```

# To read more about FOREIGN KEY constraints:
```
https://www.sqlitetutorial.net/sqlite-foreign-key/
```

ALTER TABLE application_history ADD "interview_time" DATE NOT NULL DEFAULT "HH:MM";

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


ALTER TABLE interviews ADD "user_id" INTEGER NOT NULL DEFAULT 0;