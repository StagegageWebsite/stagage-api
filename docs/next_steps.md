# Project Road Map

There are a few major steps until production

## API improvments

1. Extending the API to POST/PUT/DELETE:
  Currently the API only has implemented GET requests for artists and festivals.
  The serializers.py file need to be extended so you can create, update, and delete
  artists and festivals through the api. Estimated time: 3 hours
2. Automating the score script:
   Currently the score for artists and performances is run manually.
   This should become a cron job that gets run automatically. The script also
   needs to be updated to include the Performance model. Time estimated: 3 hours.
3. Finish testing:
   Currently testing serializers and views. Should test creating and deleteing
   serializers and views, and the score script. Time estimated: 5 hours
4. Facebook authorization
   Social authorization backend for facebook. Time estimated 1 hour.

## Infrastructure

1. Running app in production
   Hosting the API on Heroku or AWS. Estimated time: 6 hours
2. CORS framework:
   The API needs to use the CORS framework to accept requests from the frontend
   on a different host. Time estimated: 30 min
3. Logging
   App monitoring and Logging. Time estimated: 7 hours.
