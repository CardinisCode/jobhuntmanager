start:
	FLASK_APP=jhmanager FLASK_ENV=development pipenv run flask run

test:
	pipenv run pytest
