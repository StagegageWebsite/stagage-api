# Installation

## Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)

## Initialize the project
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

You probably want to create a superuser too
```bash
python stagegage_api/manage.py createsuperuser
```
