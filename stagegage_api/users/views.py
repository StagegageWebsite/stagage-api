from rest_framework import  generics
from rest_framework.authentication import BasicAuthentication
from .models import User
from .permissions import IsAuthenticatedOrCreate
from .serializers import SignUpSerializer, LoginSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAuthenticatedOrCreate]


class Login(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = (BasicAuthentication,)

    def get_queryset(self):
        return [self.request.user]
