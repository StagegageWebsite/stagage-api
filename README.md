#Stagegage Api
[![Build Status](https://travis-ci.org/StagegageWebsite/stagegage_api.svg?branch=master)](https://travis-ci.org/StagegageWebsite/stagegage_api)

Stagegage Api. Check out the project's [documentation](http://StagegageWebsite.github.io/stagegage-api/).

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb stagegage_api
```

If you need to make a git repo
```bash
git init
git remote add origin git@github.com:StagegageWebsite/stagegage_api.git
```

You can use the fabric file for running local commands or normal bash

Migrate and run the server with fabric:
```bash
fab migrate
fab run
```

You probably want to create a superuser too
```bash
python stagegage_api/manage.py createsuperuser
```

# Deployment
coming soon...

# Api Documentation
check out the [docs yo](http://StagegageWebsite.github.io/stagegage-api/api).
