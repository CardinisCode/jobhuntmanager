CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'username' TEXT NOT NULL, 'hash' TEXT NOT NULL, 'email' TEXT NOT NULL, date datetime);
CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX 'user_id' ON "users" ("id");
CREATE TABLE IF NOT EXISTS 'company_directory' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'company_name' TEXT NOT NULL);
CREATE UNIQUE INDEX 'company_id' ON "company_directory" ("id");
CREATE TABLE interview_history(
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
, "status" TEXT NOT NULL DEFAULT "upcoming");
CREATE UNIQUE INDEX 'interview_id' ON "interview_history" ("id");
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
