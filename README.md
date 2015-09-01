#stagegage_api
[![Build Status](https://travis-ci.org/StagegageWebsite/stagegage_api.svg?branch=master)](https://travis-ci.org/StagegageWebsite/stagegage_api)

Stagegage Api. Check out the project's [documentation](http://StagegageWebsite.github.io/stagegage_api/).

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

Migrate and then run
'''bash
fab migrate
fab run
'''

You'll probably want to create a superuser as well

'''bash
python stagegage_api/manage.py createsuperuser
'''

# Create Servers
By default the included fabfile will setup three environments:

- dev -- The bleeding edge of development
- qa -- For quality assurance testing
- prod -- For the live application

Create these servers on Heroku with:

```bash
fab init
```

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
