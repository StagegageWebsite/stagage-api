from django.db.models import Avg, Count
from rest_framework import serializers
from .models import *
import json

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


class FestivalListingField(serializers.RelatedField):
    """
    Custom related field to show a festival name and id
    """
    def to_representation(self, value):
        response = {'id': value.id, 'name': value.name}
        return response


class ReviewListingField(serializers.RelatedField):
    """
    Custom related field to show a review user and festival
    """
    def to_representation(self, value):
        response = {'id': value.id,
                    'user': value.user.username,
                    'festival': value.festival.name,
                    'text': value.text}
        return response

class ArtistSerializer(DynamicFieldsModelSerializer):
    """
    Artist serializer inherits from the dynamic serializer
    """

    festivals = FestivalListingField(many=True, read_only=True)
    reviews = ReviewListingField(many=True, read_only=True)
    ranking = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'created', 'name', 'festivals', 'ranking', 'reviews', 'genres')

    def get_ranking(self, obj):
        """
        Get average ranking score for the artist
        :return: ranking score as float (4.015) or 0 if no rankings
        """

        # ranking_dict returns {'score__avg': 4.0 }
        ranking_dict = Ranking.objects.filter(artist=obj).aggregate(Avg('score'))
        return ranking_dict.get('score__avg', 0)

    def get_genres(self, obj):
        """
        Get list of genres and their counts
        :return: dict of genres and counts ordered by count
            {'blues' : 5 , 'hip hop' : 4
        """
        #genre_query returns [{'genre' : 'blues' , 'votes' : 1 },...]
        genre_query = Genre.objects.values("genre").annotate(votes=Count("genre")).order_by()
        # genres = {}
        # for genre_dict in genre_query:
        #     genre_name = genre_dict['genre']
        #     genre_count = genre_dict['genre__count']
        #     genres[genre_name] = genre_count
        return genre_query




class FestivalSerializer(DynamicFieldsModelSerializer):
    """Festival serializer includes all fields."""
    artists = serializers.StringRelatedField(many=True, required=False)
    rankings = serializers.StringRelatedField(many=True, required=False)
    reviews = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Festival
        fields = ('id', 'created', 'name', 'start_date', 'artists', 'rankings', 'reviews')

