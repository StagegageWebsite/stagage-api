"""
Serializers determine what fields are passed to JSON
"""

from rest_framework import serializers
from ranking_alg import RankingAlg
from .models import Artist, Festival
from.controllers import *

class RemovableFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `remove_fields` argument that
    allows a field to be popped off
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        remove_fields = kwargs.pop('remove_fields', None)

        # Instantiate the superclass normally
        super(RemovableFieldsModelSerializer, self).__init__(*args, **kwargs)

        if remove_fields is not None:
            # Drop any fields that specified in the `remove_fields` argument.
            remove_fields = set(remove_fields)
            for field_name in remove_fields:
                self.fields.pop(field_name)


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


class ArtistSerializer(RemovableFieldsModelSerializer):
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

    Inherits from the dynamic serializer so that festivals can be poped off
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




class FestivalSerializer(RemovableFieldsModelSerializer):
    """Festival serializer includes all fields."""

    artists = ArtistSerializer(many=True)

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists')




