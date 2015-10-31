import os
import random
import string

from fabric.api import env, local, require, lcd
from fabric.colors import cyan
from fabric.operations import prompt

current_dir = os.getcwd()
env.project_name = 'stagegage_api'
env.branch = 'master'

###############################
# LOCAL SCRIPTS
###############################
def run():
    local('python manage.py runserver')


def test():
    """
    Runs nose test suite
    """
#    local('flake8 {}'.format(env.project_name))
#   print cyan('flake8 passed!', bold=True)
    local('python manage.py test stagegage')


def migrate():
    """Make local migartions"""
    local ('python manage.py makemigrations')
    print cyan('made migrations')
    local ('python manage.py migrate')


def commitpush():
    """commit and push to github"""
    local('git add .')
    local('git commit')
    local('git checkout master')
    local('git merge dev')
    local('git push origin master')
    local('git checkout dev')

def reseed():
    """delete and reseed db"""
    local('dropdb stagegage_api')
    local('createdb stagegage_api')
    migrate()
    local('python manage.py fake_data')
    local('python manage.py createsuperuser')



#######################
# Setup Heroku server
####################
def init():
    """
    Deploys servers
    """
    print cyan('Initializing...', bold=True)
    set_remotes()
    ask_for_aws_keys()
    create_standard_server()


def set_remotes():
    """
    Sets git remotes based on project structure
    """
    require('project_name')
    print cyan('Setting git remotes...')

    local('git remote add heroku git@heroku.com:{}.git'.format(env.project_name))

def ask_for_aws_keys():
    """
    Gets AWS keys from user
    """
    env.aws_access = prompt('AWS_ACCESS_KEY_ID?')
    env.aws_secret = prompt('AWS_SECRET_ACCESS_KEY?')

def create_standard_server():
    """
    Creates a sever with a standard build
    """
    create_server()
    configure_sever()
    push()
    heroku_migrate()
    create_superuser()
    ps()
    open_heroku()


def create_server():
    """
    Creates a new server on heroku
    """
    require('project_name')
    print cyan('Creating new server'.format(env.project_name))
    local('heroku create {} --buildpack https://github.com/heroku/heroku-buildpack-python'
          .format(env.project_name))


def configure_sever():
    """
    Configures server with a general configuration
    """
    local('heroku addons:create heroku-postgresql:dev')
    local('heroku pg:backups schedule DATABASE --at "04:00 UTC"')
    local('heroku pg:promote DATABASE_URL')
    local('heroku addons:create redistogo:nano')
    local('heroku addons:create zeropush:inception')
    local('heroku config:set ZEROPUSH_AUTH_TOKEN=`heroku config:get ZEROPUSH_PROD_TOKEN --remote={0}` --remote={0}')
    local('heroku addons:create newrelic:wayne')
    local('heroku config:set NEW_RELIC_APP_NAME="{}"'.format(env.project_name, env.environment))
    local('heroku config:set DJANGO_CONFIGURATION=Production')
    local('heroku config:set DJANGO_SECRET_KEY="{}"'.format(create_secret_key(), env.environment))
    set_aws_keys()


def set_key():
    local('heroku config:set DJANGO_SECRET_KEY="{}"'.format(create_secret_key()))


def deploy_docs():
    print cyan('Deploying docs...')
    local('mkdocs gh-deploy')

def push():
    require('environment')
    require('branch')

    print cyan('Pushing to Heroku...')
    require('environment')
    local('git push {} {}:master'.format(env.environment, env.branch))


def heroku_migrate():
    require('environment')
    local('heroku run python {}/manage.py migrate --remote {}'.format(env.project_name,
                                                                      env.environment))


def create_superuser():
    require('environment')
    local('heroku run python {}/manage.py '
          'createsuperuser --remote {}'.format(env.project_name, env.environment))


def ps():
    """
    Scales a web dyno on Heroku
    """
    require('environment')
    local('heroku ps:scale web=1 --remote {}'.format(env.environment))


def open_heroku():
    require('environment')
    local('heroku open --remote {}'.format(env.environment))


def set_aws_keys():
    """
    Configures S3 Keys
    """
    require('aws_access')
    require('aws_secret')
    require('project_name')

    local('heroku config:set DJANGO_AWS_ACCESS_KEY_ID={} --remote {}'
          .format(env.aws_access, env.environment))
    local('heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY={} --remote {}'
          .format(env.aws_secret, env.environment))
    local('heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME={0}-{1} --remote {1}'
          .format(env.project_name, env.environment))


def create_secret_key():
    """
    Creates a random string of letters and numbers
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(30))


def dev():
    """fab dev [command]"""
    env.environment = 'dev'
    env.branch = 'master'


def qa():
    """fab staging [command]"""
    env.environment = 'qa'
    env.branch = 'qa'


def prod():
    """fab staging [command]"""
    env.environment = 'prod'
    env.branch = 'prod'
