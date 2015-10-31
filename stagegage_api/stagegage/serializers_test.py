from rest_framework.test import APITestCase
from .factories import ArtistFactory, FestivalFactory, set_up_single
from .serializers import BaseFestivalSerializer, FestivalSerializer, BaseArtistSerializer, ArtistSerializer
from stagegage.models import Artist, Festival
from django.conf import settings

class FestivalSerializerTests(APITestCase):

  def test_baseSerializer(self):
    """Serialize a festival using the base serializer."""
    mock_fest = FestivalFactory()
    serializer = BaseFestivalSerializer(mock_fest)
    self.assertEqual(serializer.data, mock_fest.to_dict())

  def test_serialize_with_no_artists(self):
    """Serialize a festival with no artists."""
    mock_fest = FestivalFactory()
    serializer = FestivalSerializer(mock_fest)
    serializer_dict = serializer.data
    serialized_artists = serializer_dict.pop('artists')
    self.assertFalse(serialized_artists)
    self.assertEqual(mock_fest.to_dict(), serializer_dict)

  def test_serialize_with_artists(self):
    num_artists = 2
    mock_fest = FestivalFactory()
    mock_artists = ArtistFactory.create_batch(num_artists)
    mock_fest.artists.add(*mock_artists)
    serializer = FestivalSerializer(mock_fest)
    serializer_dict = serializer.data
    self.assertEqual(len(serializer.data['artists']), num_artists)

  def test_deserialize_with_no_artists(self):
    mock_fest = FestivalFactory.build()
    mock_fest_dict = {'name': mock_fest.name,
                      'start_date': mock_fest.start_date}
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
    dct = set_up_single()
    for k, v in dct.items():
      setattr(self, k, v)

  def test_baseSerializer(self):
    """Serialize a festival using the base serializer."""
    mock_artist = ArtistFactory()
    serializer = BaseArtistSerializer(mock_artist)
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

  # def test_serialize_with_artists(self):
  #   num_artists = 2
  #   mock_artist = ArtistFactory()
  #   mock_artists = ArtistFactory.create_batch(num_artists)
  #   mock_artist.artists.add(*mock_artists)
  #   serializer = FestivalSerializer(mock_artist)
  #   serializer_dict = serializer.data
  #   self.assertEqual(len(serializer.data['artists']), num_artists)

  # def test_deserialize_with_no_artists(self):
  #   mock_artist = ArtistFactory.build()
  #   mock_artist_dict = {'name': mock_artist.name,
  #                     'start_date': mock_artist.start_date}
  #   serializer = FestivalSerializer(data=mock_artist_dict)
  #   self.assertTrue(serializer.is_valid())

  # def test_deserializer_with_artists(self):
  #   mock_artist = ArtistFactory.build()
  #   mock_artists = ArtistFactory.build()
  #   mock_artist_dict = {'name': mock_artist.name,
  #                     'start_date': mock_artist.start_date,
  #                     'artists': {'name': mock_artists.name}}
  #   serializer = FestivalSerializer(data=mock_fest_dict)
  #   self.assertTrue(serializer.is_valid())