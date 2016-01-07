The Stagegage API is a RESTful API that provides the backend to the Stagegage frontend.
It is built using the Django-rest framework.

See the [API documentation](/api) for details on the api endpoints, [installation instructions](/installation)
for getting it up and running locally, [models documentation](/models) for details on the models, and the [road map](/next_steps) for what is left to be done.




# Directory Overview
## Stagegage_api
Where the business logic of the app lives

**Config:**
Different Django configurations for running in production vs. running locally.

**Contrib:**
Honestly not sure if this directory is needed.

**Scripts:**
Management commands for running one off scripts.

**Stagegage:**
Where most of the important code lives. The models, serializers, and views are probably the
most interesting

**Users:**
Where anything to do with Users lives, including user auth.

## Docs
Markdown file for documentation website. Uses the mkdocs library to create a
documentation website.

## Requirements
Third party libraries used by the API. base.txt provides the libraries used everywhere,
and then local, production, and test packages are loaded at the appropriate time.
