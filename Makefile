# target: setup - environment setup for pip and linter
setup:
	sudo apt-get install pylint
	python3 -m pip install --upgrade pip

# target: lint - linting project
lint:
	# pylint --load-plugins pylint_django --django-settings-module=library.settings inventory/*.py

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