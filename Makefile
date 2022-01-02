# target: setup - environment setup for pip
setup:
	python3 -m pip install --upgrade pip

# target: test - calls the "test" django command
test:
	python3 manage.py test

# target: clean - remove all ".pyc" files
clean:
	django-admin.py clean_pyc --settings=$(SETTINGS)

# target: update - install (and update) pip requirements
update:
	pip install -U -r requirements.txt

startdev:
	python3 manage.py runserver