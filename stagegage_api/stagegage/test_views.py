from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from .factories import ArtistFactory, FestivalFactory, RankingFactory
import json


class ArtistTests(APITestCase):
    def setUp(self):
        self.artist = ArtistFactory()

    def test_list_artists(self):
        """
        Ensure we get a list of artists with default fields
        """
        response = self.client.get('/artists/')
        # weird stuff about timezones means we have to just check the date
        response_obj = json.loads(response.content)[0]
        response_obj['created'] = response_obj['created'][:10]
        self.assertEqual(response_obj,{"id": self.artist.id,
                                         "created": str(self.artist.created)[:10],
                                         "name": self.artist.name})

    def test_list_artist_with_fields(self):
        festival = FestivalFactory(artists=(self.artist,))
        ranking = RankingFactory(artist=self.artist, festival=festival)
        response = self.client.get('/artists/?fields=festivals&fields=ranking')
        response_obj = json.loads(response.content)[0]
        response_obj['created'] = response_obj['created'][:10]
        response_obj['ranking'] = round(response_obj['ranking'], 4)
        self.assertEqual(response_obj, {'id' : self.artist.id,
                                        'created': str(self.artist.created)[:10],
                                        'name' : self.artist.name,
                                        'festivals': [{
                                            'id' : festival.id,
                                            'name' : festival.name}],
                                        'ranking': round(ranking.score, 4)})


    def test_detail_artist(self):
        """
        Ensure we get a single artist with default fields
        """
        response = self.client.get('/artists/{}/'.format(self.artist.id))
        response_obj = json.loads(response.content)
        self.assertEqual(response_obj, {"id": self.artist.id,
                                         "created": response_obj['created'],
                                         "name": self.artist.name})
