"""Define how Python model objects map to JSON objects and vice-versa.

Usage:
    artists_json = ArtistSerializer(artist_model_object)
"""
from rest_framework import serializers
from .models import Artist, Festival, Performance
from .models import Genre, Review



class BaseFestivalSerializer(serializers.ModelSerializer):
    """Festival Serializer without artists."""
    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date')


class BaseArtistSerializer(serializers.ModelSerializer):
    """Artist serializer without festivals.

    Since review and genres are computed values they are defined to be
        method fields and calculated by their respective functions.
    """
    review = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'score', 'review', 'genres')

    def get_genres(self, artist):
        """Return top 3 genres"""
        return Genre.objects.top_genres(artist)

    def get_review(self, artist):
        """Return latest review partial."""
        review = Review.objects.latest_review(artist)
        if review:
            return review.text[:100]
        return ""

class PerformanceSerializer(serializers.ModelSerializer):
    """Performance serializer."""

    class Meta:
        model = Performance
        fields = ('id', 'created', 'artist', 'score')


class ArtistSerializer(BaseArtistSerializer):
    """Same as Base serializer but includes festivals."""
    festivals = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'score', 'review', 'genres', 'festivals')

    def get_festivals(self, artist):
        festivals = artist.festival_set.all()
        ser = BaseFestivalSerializer(festivals, many=True)
        return ser.data

    # def create(self, validated_data):
    #     """Allow festivals to be created at the same time as an artist."""
    #     festivals_data = validated_data.pop('festivals')
    #     artist = Artist.objects.create(**validated_data)
    #     for festival_data in festivals_data:
    #         festival = Festival.objects.get_or_create(**festival_data)
    #         artist.festivals.add(festival)
    #     return artist


class FestivalSerializer(BaseFestivalSerializer):
    """Same as base serializer but includes artists."""
    performances = serializers.SerializerMethodField()

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'performances')

    def get_performances(self, festival):
        performances = Performance.objects.filter(festival = festival)
        ser = PerformanceSerializer(performances, many=True)
        return ser.data

    # def create(self, validated_data):
    #     artists_data = validated_data.pop('artists')
    #     festival = Festival.objects.create(**validated_data)
    #     for artist_data in artists_data:
    #         artist = Artist.objects.get_or_create(**artist_data)
    #         festival.artists.add(artist)
    #     return festival


