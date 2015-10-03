"""
Serializers determine what fields are passed to JSON
"""
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


class ArtistSerializer(BaseArtistSerializer):
    """Same as Base serializer but includes festivals."""
    festivals = BaseFestivalSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'score', 'review', 'genres', 'festivals')


    def create(self, validated_data):
        from nose.tools import set_trace; set_trace()
        festivals_data = validated_data.pop('festivals')
        artist = Artist.objects.create(**validated_data)
        for festival_data in festivals_data:
            festival = Festival.objects.get_or_create(**festival_data)
            artist.festivals.add(festival)
        return artist


class FestivalSerializer(BaseFestivalSerializer):
    """Same as base serializer but includes artists."""
    artists = serializers.SerializerMethodField()

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists')

    def get_artists(self, obj):
        artists = Artist.objects.filter(festivals=obj).order_by('-score')
        ser = BaseArtistSerializer(artists, many=True)
        return ser.data

    def validate(self, attrs):
        from nose.tools import set_trace; set_trace()
        return attrs

    def create(self, validated_data):
        artists_data = validated_data.pop('artists')
        festival = Festival.objects.create(**validated_data)
        for artist_data in artists_data:
            artist = Artist.objects.get_or_create(**artist_data)
            festival.artists.add(artist)
        return festival


