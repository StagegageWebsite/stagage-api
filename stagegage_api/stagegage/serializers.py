"""
Serializers determine what fields are passed to JSON
"""
from django.db.models import Count
from rest_framework import serializers
from .models import Artist, Festival
from .models import Genre, Review



class BaseFestivalSerializer(serializers.ModelSerializer):
    """Festival Serializer without artists."""
    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date')


class BaseArtistSerializer(serializers.ModelSerializer):
    """Artist serializer without festivals."""
    review = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'ranking', 'review', 'genres')

    def get_ranking(self, artist):
        """
        get order of artist in list
        """
        return self.instance.index(artist) + 1


    def get_genres(self, artist):
        """Return top 3 genres"""
        return Genre.objects.top_genres(artist)

    def get_review(self, artist):
        """Return latest review partial."""
        review = Review.objects.latest_review(artist)
        return review.text[:100]


class ArtistSerializer(BaseArtistSerializer):
    """Same as Base serializer but includes festivals."""
    festivals = BaseFestivalSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'ranking', 'review', 'genres', 'festivals')



class FestivalSerializer(BaseFestivalSerializer):
    """Same as base serializer but includes artists."""
    artists = serializers.SerializerMethodField()

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists')

    def get_artists(self, obj):
        artists = Artist.objects.filter(festivals=obj).rank()
        ser = BaseArtistSerializer(artists, many=True)
        return ser.data


