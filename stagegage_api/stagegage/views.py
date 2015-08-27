from .models import *
from .serializers import *
from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for viewing and editing artists
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class FestivalViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for viewing and editing festivals
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer


class RankingViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for viewing and editing rankings
    """
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for viewing and editing reviews
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class GenreViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for viewing and editing genres
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer