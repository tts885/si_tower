#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:40:56 2022

@author: guangdong.chen
"""

from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'work', views.WorkViewSet)

urlpatterns = [
    path('api/chart/', views.ChartData.as_view()),

    ]
urlpatterns = format_suffix_patterns(urlpatterns)
