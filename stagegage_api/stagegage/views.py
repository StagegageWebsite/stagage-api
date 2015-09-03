from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class ArtistViewSet(viewsets.ModelViewSet):
    """
    Views for interacting with the Artist model
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]


    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Respond with a single artist
        Pass GET params to the serializer
        """
        fields = get_fields(request)
        artist = get_object_or_404(self.queryset, pk=pk)
        serializer = ArtistSerializer(artist, fields=fields)
        return Response(serializer.data)


class FestivalViewSet(viewsets.ModelViewSet):
    """
    Views for interacting with the Festival Model
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        fields = get_fields(request)
        serializer = FestivalSerializer(self.queryset, many=True, fields=fields)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        fields = get_fields(request)
        festival = get_object_or_404(self.queryset, pk=pk)
        serializer = FestivalSerializer(festival, fields=fields)
        return Response(serializer.data)




def get_fields(request):
    """Helper method to get fields"""
    default_fields = ['id', 'created', 'name']
    extra_fields = request.QUERY_PARAMS.getlist('fields')
    return default_fields + extra_fields