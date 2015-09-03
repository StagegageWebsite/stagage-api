from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class ArtistList(generics.ListAPIView):
    """
    List of artists and associated data
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update, and Delete view for an artist
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]




class FestivalList(generics.ListAPIView):
    """
    List of festivals with associated data
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [AllowAny]


class FestivalDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update, and delete view for a festival
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [AllowAny]

