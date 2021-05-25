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
    'name' TEXT NOT NULL,
    'description' BLOB DEFAULT "N/A",
    'location' TEXT DEFAULT "N/A",
    'industry' TEXT DEFAULT "N/A",
    'url' TEXT DEFAULT "N/A",
    'interviewers' TEXT DEFAULT "Unknown at present",
    'contact_number' TEXT DEFAULT "Unknown at present",
    FOREIGN KEY (user_id) REFERENCES users (user_id)   
);

CREATE TABLE interview_preparation(
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

CREATE TABLE company_notes(
    'company_note_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'date' DATETIME NOT NULL, 
    'subject' TEXT NOT NULL,
    'note_text' BLOB DEFAULT "N/A",
    FOREIGN KEY (user_id) REFERENCES users (user_id)
    FOREIGN KEY (company_id) REFERENCES company (company_id)
);

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

CREATE TABLE indiv_contacts( 
    'contact_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'full_name' TEXT NOT NULL,
    'job_title' TEXT NOT NULL,
    'contact_number' TEXT DEFAULT "N/A",
    'company_name' TEXT DEFAULT "N/A",
    'email_address' TEXT DEFAULT "N/A",
    'linkedin_profile' TEXT DEFAULT "N/A",
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
);

CREATE TABLE interviews(
    'interview_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'application_id' INTEGER NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'entry_date' DATETIME NOT NULL, 
    'interview_date' DATETIME NOT NULL, 
    'interview_time' DATETIME NOT NULL,
    'interview_type' TEXT NOT NULL,
    'interview_location' TEXT NOT NULL DEFAULT "Remote",
    'interview_medium' TEXT,
    'other_medium' TEXT DEFAULT "N/A",
    'contact_number' TEXT DEFAULT "N/A",
    'status' TEXT NOT NULL DEFAULT "upcoming",
    'interviewer_names' TEXT DEFAULT "Unknown at present", 'video_link' BLOB DEFAULT "N/A",
    'extra_notes' BLOB DEFAULT "N/A",
    FOREIGN KEY (application_id) REFERENCES applications (application_id), 
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE job_offers(
    'job_offer_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'application_id' INTEGER NOT NULL, 
    'entry_date' DATETIME NOT NULL,
    'job_role' TEXT NOT NULL,
    'starting_date' DATETIME NOT NULL, 
    'salary_offered' TEXT NOT NULL,
    'perks_offered' TEXT NOT NULL,
    'offer_response' TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id), 
    FOREIGN KEY (company_id) REFERENCES company (company_id),
    FOREIGN KEY (application_id) REFERENCES job_applications (application_id)
);

CREATE TABLE job_applications(
    'application_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 
    'company_id' INTEGER NOT NULL, 
    'app_date' DATETIME NOT NULL, 
    'app_time' TIME NOT NULL,
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
