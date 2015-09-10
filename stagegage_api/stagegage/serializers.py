"""
Serializers determine what fields are passed to JSON
"""

from rest_framework import serializers
from .models import Artist, Festival
from.controllers import *
from .ranking_alg import RankingAlgorithm


class BaseFestivalSerializer(serializers.ModelSerializer):
    """Festival serializer includes all fields."""
    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date')


class BaseArtistSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'ranking', 'review', 'genres')

    def get_ranking(self, obj):
        """
        Get average ranking score for the artist
        :return: ranking score as float (4.015) or 0 if no rankings
        """
        ranking_alg = self.context.get('ranking_alg')
        return ranking_alg.get_rank(obj.id)

    def get_genres(self, obj):
        return top_genres(obj)

    def get_review(self, obj):
        return "hello"


class ArtistSerializer(BaseArtistSerializer):
    festivals = BaseFestivalSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'ranking', 'review', 'genres', 'festivals')



class FestivalSerializer(BaseFestivalSerializer):

    artists = serializers.SerializerMethodField()

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists')

    def get_artists(self, obj):
        artists = Artist.objects.filter(festivals=obj)
        ranking_alg = RankingAlgorithm(festival=obj)
        ser = BaseArtistSerializer(artists, many=True, context={'ranking_alg': ranking_alg})
        return sorted(ser.data, key=lambda s: s['ranking'])


