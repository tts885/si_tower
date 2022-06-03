from django.shortcuts import render

# Create your views here.
import django_filters

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from apps.accounts.models import CustomUser
from apps.pms.models.Work import Work
from .serializer import UserSerializer,WorkSerializer

def index(request):
    return HttpResponse("Hello, world.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
