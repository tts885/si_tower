#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:40:56 2022

@author: guangdong.chen
"""

from django.urls import path
from rest_framework import routers
from . import views

app_name = 't90_api'

urlpatterns = [
    path('', views.index, name='index'),

    ]
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
