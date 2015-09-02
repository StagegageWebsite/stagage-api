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
		"name": "Artist 1"
	},
]
```

optionally you can get the festivals, reviews, ranking, or genres associated with each artist.

Request each optional field by including them as a field paramater in the GET request

GET [/artists/?fields=festivals&fields=reviews=&fields=ranking&fields=genres](#)

```json
[
	{
		"id": 1,
		"created": "2015-08-29T15:55:06+0000",
		"name": "Artist 1",
		"festivals": [
			{
			    "id" : 1,
			    "name" : "Festival 1"
			},
		],
		"ranking": 4.0,
		"reviews": [
			 {
                "festival": "Festival 1",
                "text": "great",
                "id": 1,
                "user": "admin"
            },
		],
		"genres" : [
			{
                "genre": "blues",
                "votes": 5
            },
		]
	}
]
```

To get the records for a single artist just put the id of the artist in the url

GET [/artists/1/](#)

The same optional field paramaters apply

# Festivals

GET [/festivals/](#)

```json
[
	{
        "id": 1,
        "created": "2015-08-29T15:55:29+0000",
        "name": "Festival 1"
    },
]
```

you can also get the artists, reviews, and rankings associated with a festival in the same manner
as an artist.

GET [/festivals/?fields=artists&fields=rankings&fields=reviews](#)

```json
[
	{
		"id": 1,
        "created": "2015-08-29T15:55:29+0000",
        "name": "Festival 1",
        "artists": [
            "Artist 1",
            "Artist 2"
        ],
        "rankings": [
            "admin : Artist 1 : Festival 1 : 3.000000",
        ],
        "reviews": [
            "great",
        ]
    }
]
```




