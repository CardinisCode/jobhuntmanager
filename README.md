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

# Adding values to a table in SQLite3
```
"INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", (username, hashed_password, email))
```

