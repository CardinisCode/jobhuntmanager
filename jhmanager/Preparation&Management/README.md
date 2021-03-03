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


# Requirements:
```
fontawesome-free==0.1.5
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

# To install FontAwesome: 
```
pip3 install Flask-FontAwesome
```








