from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from .factories import *
from users.factories import UserFactory
import json


class ArtistTests(APITestCase):
    def setUp(self):
        artist = ArtistFactory()
        festival = FestivalFactory(artists=[artist])
        user = UserFactory()
        ranking_set = RankingSetFactory()
        ranking = RankingFactory()
        genre = GenreFactory()
        review = ReviewFactory()

        ranking_set.festival = festival
        ranking_set.user = user
        ranking.ranking_set = ranking_set
        ranking.artist = artist
        genre.user = user
        genre.artist = artist

        self.artist = artist
        self.festival = festival
        self.ranking = ranking
        self.genre = genre
        self.review = review


    def test_list_artists(self):
        from nose.tools import set_trace; set_trace()
        response = self.client.get(reverse('artist_list'))
        response_obj = json.loads(response.content)[0]
        response_obj['created'] = response_obj['created'][:10]
        self.assertEqual(response_obj, {'id': self.artist.id,
                                        'created': str(self.artist.created)[:10],
                                        'name': self.artist.name,
                                        'festivals': [{
                                            'id': self.festival.id,
                                            'name': self.festival.name}],
                                        'ranking': self.ranking,
                                        'genres': [self.genre.genre],
                                        'review': self.review.text
                                        })


    def test_detail_artist(self):
        """
        Ensure we get a single artist with default fields
        """
        pass