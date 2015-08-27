from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    """Artist serializer. Includes list of festivals"""

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'festivals')


class FestivalSerializer(serializers.ModelSerializer):
    """Festival serializer includes all fields."""

    class Meta:
        model = Festival


class RankingSerializer(serializers.ModelSerializer):
    """Rankings serializer."""

    class Meta:
        model = Ranking


class ReviewSerializer(serializers.ModelSerializer):
    """Review serializer."""

    class Meta:
        model = Review


class GenreSerializer(serializers.ModelSerializer):
    """Genre serializer."""

    class Meta:
        model = Genre