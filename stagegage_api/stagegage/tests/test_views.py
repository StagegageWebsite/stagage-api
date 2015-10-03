from django.core.urlresolvers import reverse
from django.conf import settings
from rest_framework.test import APITestCase
from rest_framework import status
from .factories import set_up_single, set_up_many, ArtistFactory, FestivalFactory
from stagegage.models import Artist, Festival
import json


class ArtistTests(APITestCase):
    def setUp(self):
        """Set up a single instance of each model and assign to self."""
        dct = set_up_single()
        for k,v in dct.items():
            setattr(self, k, v)

        self.test_dict = {'id': self.artist.id,
                          'created': format_date(self.artist.created),
                          'name': self.artist.name,
                          'score': self.artist.score,
                          'genres': [self.genre.genre],
                          'review': self.review.text[:100],
                          'festivals': [
                              {'id': self.festival.id,
                               'name': self.festival.name,
                               'start_date': self.festival.start_date,
                               'created': format_date(self.festival.created)}]}
        self.client.force_authenticate(user=self.user)


    def test_list(self):
        """Test """
        response = self.client.get(reverse('artists-list'))
        response_dict = json.loads(response.content)['results']
        self.assertEqual(response_dict, [self.test_dict])

    def test_create(self):
        artist = ArtistFactory.build()
        f1 = FestivalFactory()
        f2 = FestivalFactory.build()

        data = {'name': artist.name, 'festivals': [
            {'name': f1.name, 'start_date': f1.start_date},
            {'name': f2.name, 'start_date': f2.start_date}]}
        from nose.tools import set_trace; set_trace()
        response = self.client.post(reverse('artists-list'), data)
        created_artist = Artist.objects.get(name=artist.name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(artist), str(created_artist))
        self.assertEqual(created_artist.festivals.count(), 2)

    def test_retrieve(self):
        response = self.client.get(reverse('artists-detail', args=(self.artist.id,)))
        response_dict = json.loads(response.content)
        self.assertEqual(response_dict, self.test_dict)


    def test_update(self):
        new_artist = ArtistFactory.build()
        data = {'name': new_artist.name}
        url = reverse('artists-detail', args=(self.artist.id,))
        response = self.client.patch(url, data)
        updated_artist = Artist.objects.get(name=new_artist.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_artist.name, new_artist.name)

    def test_destroy(self):
        new_artist = ArtistFactory()
        count = Artist.objects.count()
        url = reverse('artists-detail', args=(new_artist.id,))
        response = self.client.delete(url)
        new_count = Artist.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(count-1, new_count)


    def test_auth(self):
        self.client.force_authenticate()
        url = reverse('artists-detail', args=(self.artist.id,))
        response = self.client.patch(url, {'name': 'name'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)


class FestivalTest(APITestCase):

    def setUp(self):
        dct = set_up_single()
        for k,v in dct.items():
            setattr(self, k, v)

        self.test_dict = {'id': self.festival.id,
                          'name': self.festival.name,
                          'start_date': self.festival.start_date,
                          'created': format_date(self.festival.created),
                          'artists': [
                               {'id': self.artist.id,
                                'created': format_date(self.artist.created),
                                'name': self.artist.name,
                                'score': self.artist.score,
                                'genres': [self.genre.genre],
                                'review': self.review.text[:100]}]}

        self.client.force_authenticate(user=self.user)


    def test_list(self):
        """List of festivals with artists."""
        response = self.client.get(reverse('festivals-list'))
        response_dict = json.loads(response.content)['results']
        self.assertEqual(response_dict, [self.test_dict])

    def test_create(self):
        #TODO: nested create
        artists = ArtistFactory.build_batch(10)
        artist_data = [{'name': artist.name} for artist in artists]
        festival = FestivalFactory.build()
        data = {'name' : festival.name,
                'start_date': festival.start_date,
                'artists': artist_data}
        response = self.client.post(reverse('festivals-list'), data)
        created_festival = Festival.objects.get(name=festival.name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(festival), str(created_festival))
        self.assertEqual(created_festival.artists.count(), len(artists))


    def test_update(self):
        new_festival = FestivalFactory.build()
        data = {'name': new_festival.name}
        url = reverse('festivals-detail', args=(self.festival.id,))
        response = self.client.patch(url, data)
        updated_festival = Festival.objects.get(name=new_festival.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_festival.name, new_festival.name)

    def test_destroy(self):
        new_festival = FestivalFactory()
        count = Festival.objects.count()
        url = reverse('festivals-detail', args=(new_festival.id,))
        response = self.client.delete(url)
        new_count = Festival.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(count-1, new_count)


    def test_auth(self):
        self.client.force_authenticate()
        url = reverse('festivals-detail', args=(self.festival.id,))
        response = self.client.patch(url, {'name': 'name'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)


def format_date(date):
    return date.strftime(settings.REST_FRAMEWORK['DATETIME_FORMAT'])