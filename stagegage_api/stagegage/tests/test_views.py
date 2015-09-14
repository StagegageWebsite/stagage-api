from django.core.urlresolvers import reverse
from django.conf import settings
from rest_framework.test import APITestCase
from .factories import set_up_single, set_up_many
import json



class ArtistTests(APITestCase):
    def setUp(self):
        """Set up a single instance of each model and assign to self."""
        dct = set_up_single()
        for k,v in dct.items():
            setattr(self, k, v)

    def test_list_artists(self):
        """Test """
        response = self.client.get(reverse('artist_list'))
        response_dict = json.loads(response.content)['results'][0]
        test_dict = {'id': self.artist.id,
                     'created': format_date(self.artist.created),
                     'name': self.artist.name,
                     'ranking': 1,
                     'genres': [self.genre.genre],
                     'review': self.review.text[:100],
                     'festivals': [{'id': self.festival.id,
                                    'name': self.festival.name,
                                    'start_date': self.festival.start_date,
                                    'created': format_date(self.festival.created)}]}
        self.assertEqual(response_dict, test_dict)


class FestivalTests(APITestCase):
    maxDiff = None
    def setUp(self):
        """Set up a single instance of each model and assign to self."""
        for k,v in set_up_single().items():
            setattr(self, k, v)


    def test_list_festivals(self):
        """List of festivals with artists."""
        response = self.client.get(reverse('festival_list'))
        response_dict = json.loads(response.content)['results'][0]
        test_dict = {'id': self.festival.id,
                     'created': format_date(self.festival.created),
                     'start_date': self.festival.start_date,
                     'name': self.festival.name,
                     'artists': [{'id': self.artist.id,
                                  'name': self.artist.name,
                                  'created': format_date(self.artist.created),
                                  'ranking': 0,
                                  'genres': [self.genre.genre],
                                  'review': self.review.text[:100]}]}
        self.assertEqual(response_dict, test_dict)


def format_date(date):
    return date.strftime(settings.REST_FRAMEWORK['DATETIME_FORMAT'])