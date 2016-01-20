"""Views for the models.

We are using viewsets for our models that have most of the endpoints already
defined.
"""
from .models import Artist, Festival
from .permissions import IsAdminOrReadOnly
from .serializers import ArtistSerializer, FestivalSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
    """Viewset for artists."""
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        #TODO: filter by festivals
        return Artist.objects.all().order_by('-score')



class FestivalViewSet(viewsets.ModelViewSet):
    """Viewset for Festivals."""
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [IsAdminOrReadOnly]



