"""
Serializers determine what fields are passed to JSON
"""

from rest_framework import serializers
from ranking_alg import RankingAlg
from .models import Artist, Festival
from.controllers import *



class FestivalListingField(serializers.RelatedField):
    """
    Custom related field to show a festival
    """
    def to_representation(self, value):
        response = {'id': value.id,
                    'created': value.created,
                    'name': value.name,
                    'start_date': value.start_date}
        return response


class ArtistListingField(serializers.RelatedField):
    """
    Custom related field to show an artist
    """
    def to_representation(self, value):
        ranking_alg = RankingAlg(value)
        response = {'id': value.id,
                    'created': value.created,
                    'name': value.name,
                    'ranking': ranking_alg.ranking(),
                    'review': "hello",
                    'genres': top_genres(value)}
        return response


class ArtistSerializer(serializers.ModelSerializer):
    """
    By default Artist serializer responds with JSON
    {
        'id': 1,
        'created' : 20015-1-1,
        'name': 'abc'
        'festivals' : <see festival listing field>
        'ranking' : <see ranking alg>
        'review' : 'abc',
        'genres' : ['abc', 'abc', 'abc']
    """

    festivals = FestivalListingField(many=True, read_only=True)
    review = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'festivals', 'ranking', 'review', 'genres')

    def get_ranking(self, obj):
        """
        Get average ranking score for the artist
        :return: ranking score as float (4.015) or 0 if no rankings
        """
        ranking_alg = RankingAlg(obj)
        return ranking_alg.ranking()

    def get_genres(self, obj):
        return top_genres(obj)

    def get_review(self, obj):
        return "hello"




class FestivalSerializer(serializers.ModelSerializer):
    """Festival serializer includes all fields."""
    artists = ArtistListingField(many=True, read_only=True)

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists')





