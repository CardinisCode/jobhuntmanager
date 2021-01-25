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

ALTER TABLE application_history ADD "salary" TEXT NOT NULL DEFAULT "N/A";