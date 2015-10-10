from .models import Artist, Festival
from .serializers import ArtistSerializer, FestivalSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets




class ArtistViewSet(viewsets.ModelViewSet):
    """
    Viewset for artists
    """
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        #TODO: filter by festivals
        return Artist.objects.all().order_by('-score')



class FestivalViewSet(viewsets.ModelViewSet):
    """
    List of festivals with associated data
    """
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [IsAdminOrReadOnly]



