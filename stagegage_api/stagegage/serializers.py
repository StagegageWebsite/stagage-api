from rest_framework import serializers
from .models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ArtistSerializer(DynamicFieldsModelSerializer):
    """Artist serializer"""
    festivals = serializers.StringRelatedField(many=True, required=False)
    rankings = serializers.StringRelatedField(many=True, required=False)
    reviews = serializers.StringRelatedField(many=True, required=False)
    genres = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'festivals', 'rankings', 'reviews', 'genres')

class FestivalSerializer(DynamicFieldsModelSerializer):
    """Festival serializer includes all fields."""
    artists = serializers.StringRelatedField(many=True, required=False)
    rankings = serializers.StringRelatedField(many=True, required=False)
    reviews = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists', 'rankings', 'reviews')


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