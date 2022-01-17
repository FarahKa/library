# target: setup - environment setup for pip and linter
setup:
	# apt-get install pylint
	python3 -m pip install --upgrade pip

# target: lint - linting project
lint:
	# pylint --load-plugins pylint_django --django-settings-module=library.settings inventory/*.py

# target: test - calls the "test" django command
test:
	python3 ./manage.py test  --keepdb

# target: clean - remove all ".pyc" files
clean:
	django-admin.py clean_pyc --settings=$(SETTINGS)

# target: update - install (and update) pip requirements
update:
	pip install -U -r ./requirements.txt

# target: startdev - start project in development
startdev:
	python3 ./manage.py runserver