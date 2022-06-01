from django.shortcuts import render

# Create your views here.
import django_filters

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from apps.t01_accounts.models import CustomUser
from .serializer import UserSerializer

def index(request):
    return HttpResponse("Hello, world.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer