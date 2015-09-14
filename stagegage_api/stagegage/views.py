from .models import Artist, Festival
from .serializers import ArtistSerializer, FestivalSerializer
from .permissions import IsAdminOrReadOnly

from rest_framework import viewsets




class ArtistViewSet(viewsets.ModelViewSet):
    """
    Viewset for artists
    """
    queryset = Artist.objects.all().rank()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]




class FestivalViewSet(viewsets.ModelViewSet):
    """
    List of festivals with associated data
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [IsAdminOrReadOnly]



