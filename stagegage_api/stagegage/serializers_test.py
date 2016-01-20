from django.conf import settings
from rest_framework.test import APITestCase
from stagegage.factories import ArtistFactory,
from stagegage.factories import ArtistFactory,FestivalFactory, set_up_single
from .serializers import BaseFestivalSerializer, FestivalSerializer, BaseArtistSerializer, ArtistSerializer
from stagegage.models import Artist, Festival

class FestivalSerializerTests(APITestCase):

  def setUp(self):
    self.test_festival = FestivalFactory.buid()
    self.test_festival_dict = {
      'id': self.test_festival.id,
      'created': format_date(self.test_festival.created),
      'name': self.test_festival.name,
      'start_date': self.test_festival.start_date,
      'performances': []
    }

  def test_simple_serialize(self):
    """Serialize a festival using the base serializer."""
    serializer = FestivalSerializer(self.test_festival)
    self.assertEqual(serializer.data, self.test_festival_dict)

  def test_create_artists(self):
    test_artists = ArtistFactory.create_batch(2)
    self.test_festival.artists.add(*mock_artists)
    serializer = FestivalSerializer(mock_fest)
    serializer_dict = serializer.data
    self.assertEqual(len(serializer.data['artists']), num_artists)

  def test_artists_already_exist(self):
    test_artists = ArtistFactory.create(2)
    self.test_festival.artists.add(*mock_artists)
    serializer = FestivalSerializer(mock_fest)
    serializer_dict = serializer.data
    self.assertEqual(len(serializer.data['artists']), num_artists)

  def test_deserialize_with_no_artists(self):
    mock_fest_dict = {'name': self.test_festival.name,
                      'start_date': self.test_festival.start_date}
    serializer = FestivalSerializer(data=mock_fest_dict)
    self.assertTrue(serializer.is_valid())

  def test_deserializer_with_artists(self):
    mock_fest = FestivalFactory.build()
    mock_artists = ArtistFactory.build()
    mock_fest_dict = {'name': mock_fest.name,
                      'start_date': mock_fest.start_date,
                      'artists': {'name': mock_artists.name}}
    serializer = FestivalSerializer(data=mock_fest_dict)
    self.assertTrue(serializer.is_valid())

class ArtistSerializerTests(APITestCase):
  def setUp(self):
    self.test_artist = ArtistFactory.build()
    self.test_artist_dict = {
      'id': self.test_artist.id,
      'created': format_date(self.test_artist.created),
      'name': self.test_artist.name,
      'score': self.test_artist.score
    }

  def test_baseSerializer(self):
    """Serialize a festival using the base serializer."""
    serializer = BaseArtistSerializer(self.test_artist)
    serializer_dict = serializer.data
    serializer_dict.pop('genres')
    serializer_dict.pop('review')
    self.assertEqual(serializer_dict, mock_artist.to_dict())

  def test_serialize_with_festivals(self):
    """Serialize a festival with no artists."""
    mock_artist = self.artist
    mock_dict = mock_artist.to_dict()
    mock_dict['genres'] = (self.genre.genre)
    mock_dict['review'] = self.review.text[:100]
    mock_dict['festivals'] = [self.festival.to_dict()]
    serializer = ArtistSerializer(mock_artist)
    serializer_dict = serializer.data
    # from nose.tools import set_trace; set_trace()
    serializer_dict['festivals'][0] = dict(serializer_dict['festivals'][0])
    serializer_dict['genres'] = serializer_dict['genres'][0]
    self.assertEqual(mock_dict, serializer_dict)

  def test_deserialize_with_no_artists(self):
    mock_artist = ArtistFactory.build()
    mock_artist_dict = {'name': mock_artist.name,
                      'start_date': mock_artist.start_date}
    serializer = FestivalSerializer(data=mock_artist_dict)
    self.assertTrue(serializer.is_valid())

  def test_deserializer_with_artists(self):
    mock_artist = ArtistFactory.build()
    mock_artists = ArtistFactory.build()
    mock_artist_dict = {'name': mock_artist.name,
                      'start_date': mock_artist.start_date,
                      'artists': {'name': mock_artists.name}}
    serializer = FestivalSerializer(data=mock_fest_dict)
    self.assertTrue(serializer.is_valid())


def format_date(date):
    return date.strftime(settings.REST_FRAMEWORK['DATETIME_FORMAT'])

