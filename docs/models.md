# Stagegage Models

There are a few models that comprise the core of the Stagegage API

## Artists
Keeps track of the artist name and the overall artist score. Since the
score is not a simple average of all rankings it is difficult to
calculate on the fly using the Django ORM. The current solution is to
have a sperate python script to calculate the proper score and write
to the database.
The script lives in stagegeage_api/scripts/management/commands/score.py.
Next steps would be to automate this script to run as a cron job.

## Festivals
Keeps track of the festival name and start date.

## Performances
Creates a many to many relationship between festivals and artists. A single
artist performs at many festivals, and a single festival has many artists.
This model also keeps track of the artist's performance score. This is a
combination of all the user rankings for that artist at a specific festival.
Notice that this is different from the overall artists score that is kept
track by the artist model.

## Ranking Sets
Groups together a set of rankings by a single user for all the artists they
review at a single festival.

## Rankings
Keeps track of the actual numerical score for an artist by a user. Grouped together
in a Ranking Set model.

## Reviews
Text review of an artist, similar to a Yelp review. This review has no impact on
the artist or performance score.

## Genres
Along with a text review, an User can also choose to label an artist under one
or more genres, selected from a predefined list of choices.

## User
Keeps track of users that sign up on the site, and associates an auth token with them.