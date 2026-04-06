from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated, IsAdmin]

