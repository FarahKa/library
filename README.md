# What is this?

This is a web app written to test out and learn devops and ci/cd techniques.
The webservices on the **django restful** framework. They let you submit, list and modify authors and books. 
The unit tests for these webservices use the django restful **API test cases**.
These tests are ran every time code is pushed to the **main** branch. This is thanks to github actions and workflows. The tests run on multiple python versions.
A **github package** is also created each time code is pushed to main. This package is a docker image that can be used to deploy the app.


# How to run this?


## Local development environment
You need python 3.7 to 3.9 to run this app. 
First you install all requirements:

    pip install -r requirements.txt

Second you run all migrations:

    python manage.py makemigrations
    python manage.py migrate

Last you run the app:

    python manage.py runserver


## Local docker image

You need docker on your machine.
First you build the image (you can optionally tag it):

    docker build .
 Then you get the image ID and run the image:
 

    docker images
    docker run -p 8000:8000 [imageID]

## From a github packages image

You need docker to pull the image.
Visit this page: https://github.com/FarahKa/library/pkgs/container/library to get the version you need. Each package hash is a commit hash.

    docker pull ghcr.io/farahka/library:sha-5ba9004
Then run the image locally like above.

# Project structure

Important root folder files are:

 - Local .env file containing secrets.
 - Local sqlite database.
 - DOCKERFILE for image building.
 - manage.py for project running
 - Makefile for command abstraction
 - requirements.txt for required python libraries.
 
 The **.github/workflows** folder contains two workflows:
 - django.yml for continuous integration: running tests
 - release.yml for building the github package
 
The **library** folder contains the app settings and routes.
The **inventory** folder contains the webservices, models and tests.



