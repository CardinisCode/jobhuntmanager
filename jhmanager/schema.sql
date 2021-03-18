BEGIN TRANSACTION;
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS 'test' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS 'users' (
    'user_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'username' TEXT NOT NULL, 
    'hash' TEXT NOT NULL, 
    'email' TEXT NOT NULL, 
    'date' datetime
);

CREATE TABLE IF NOT EXISTS 'company' (
    'company_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'description' TEXT DEFAULT "N/A",
    'location' TEXT DEFAULT "N/A",
    'industry' TEXT DEFAULT "N/A",
    'url' TEXT DEFAULT "N/A",
    'interviewers' TEXT DEFAULT "Unknown at present",
    'contact_number' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (user_id) REFERENCES users (user_id)   
);

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

CREATE TABLE IF NOT EXISTS 'interviews' (
    'interview_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'application_id' INTEGER NOT NULL,
    'date' DATETIME NOT NULL, 
    'time' DATETIME NOT NULL,
    'interview_type' TEXT NOT NULL, 
    'interview_location' TEXT DEFAULT "Remote",
    'interview_medium' TEXT,
    'other_medium' TEXT DEFAULT "N/A",
    'contact_number' TEXT DEFAULT "N/A",
    'status' TEXT NOT NULL DEFAULT "upcoming",
    'interviewer_names' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (application_id) REFERENCES applications (application_id)
);
COMMIT;

CREATE TABLE IF NOT EXISTS 'application_notes' (
    'app_notes_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'application_id' INTEGER NOT NULL,
    'company_id' INTEGER NOT NULL, 
    'entry_date' DATETIME NOT NULL,
    'description' TEXT NOT NULL,
    'notes_text' BLOB DEFAULT "N/A",
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (application_id) REFERENCES job_applications (application_id),
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);