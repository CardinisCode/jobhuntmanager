This Should detail what your project is about and what problem your program will solve

## Getting Started

Setup environment variables, in the terminal copy and enter these lines of code:

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

# Using a 'a' reference and just style it to look like a button

```
<a href="https://google.com" class="button">Go to Google</a>
```

# Adding a column to an existing table in SQLite3
```
ALTER TABLE users ADD date datetime;
```