# Exploring the API

there are two good ways to explore the api

## Browsable API
Django has a built it browsable api. Simply start the webserver and navigate to the appropriate url in the browser. You should be able to test the api and see results right there.

## API Docs
There are automatically created docs on all the api endpoints. Start the webserver and navigate to [localhost:8000/docs](localhost:8000/docs). This shows a list of all the api endpoints and the accepted method types

# JSON Responses

## Artist
a GET request to [/artists](#) returns a list of all the artists

```json
[
	{
		"id": 1,
		"created": "2015-08-29T15:55:06+0000",
		"name": "Artist 1",
    "score": 6.7,
    "review": "best band ever.",
    "genres": ["rock", "pop", "jazz"],
    festivals: [
      {
        "id": 3,
        "created": "2016-01-02T21:40:28+0000",
        "name": "Festival 3",
        "start date": "2016-05-02"
      }]
	},
]
```

To get the records for a single artist just put the id of the artist in the url

GET [/artists/1/](#)


# Festivals

GET [/festivals/](#)

```json
[
	{
        "id": 1,
        "created": "2015-08-29T15:55:29+0000",
        "name": "Festival 1"
        "start_date": "2016-02-01",
        "performances": [
          {
            "id": 5
            "created": "2016-01-02T21:41:28+0000",
            "artist": 5,
            "score": 1.9
          }]
    },
]
```

GET [/festivals/]1(#)
Returns a single festival


