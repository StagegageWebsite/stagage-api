from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .ranking_alg import RankingAlgorithm
from rest_framework.response import Response
from rest_framework import filters


class ArtistList(APIView):
    """
    List of artists and associated data
    """
    permission_classes = [AllowAny]

    def get(self, request):
        ranking_alg = RankingAlgorithm()
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True, context={'ranking_alg': ranking_alg})
        return Response(sorted(serializer.data, key=lambda s: s['ranking']))


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

