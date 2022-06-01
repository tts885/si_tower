#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:40:56 2022

@author: guangdong.chen
"""
from apps.pms import views
from django.urls import path, re_path

app_name = 'pms'

urlpatterns = [
    # HTML Template
    re_path(r'^.*\.html', views.html, name='pms'),
    path('demo/', views.demo, name='demo'),

    # Portal
    path('pms/', views.index, name='pms'),
    # path('', views.portal, name='portal'),

    # PM
    # 01>>>Select Model
    path('pms/select_model/', views.select_model, name='select_model'),

    # 02>>>Search Dispatch
    # path('search_dispatch/', views.search_dispatch, name='search_dispatch'),
    path('search/', views.initial_view, name='search'),

    # Work
    path('pms/work/search', views.SearchWork.as_view(), name='work_search'),
    path('pms/work/create/', views.CreateWork.as_view(), name='work_Create'),
    path('pms/work/update/<int:pk>/', views.UpdateWork.as_view(), name='work_Update'),
    path('pms/work/getIssue/', views.Work_GetIssue.as_view(), name='getIssue'),
    path('pms/work/addRelation/', views.AddRelation_toWork.as_view(), name='addRelation_work'),
    path('pms/work/removeRelation/<int:object_pk>/<int:record_pk>/',
         views.RemoveRelation_fromWork.as_view(), name='removeRelation_work'),

    # Issue
    path('pms/issue/search', views.SearchIssue.as_view(), name='issue_search'),
    path('pms/issue/create/', views.CreateIssue.as_view(), name='issue_Create'),
    path('pms/issue/update/<int:pk>/', views.UpdateIssue.as_view(), name='issue_Update'),

    path('pms/issue/getWork/', views.Issue_GetWork.as_view(), name='issue_GetWork'),
    path('pms/issue/addRelation/', views.AddRelation_toIssue.as_view(), name='addRelation_issue'),
    path('pms/issue/removeRelation/<int:object_pk>/<int:record_pk>/',
         views.RemoveRelation_fromIssue.as_view(), name='removeRelation_issue'),

    # path('lode_issue_data/', views.loda_issue_data.as_view(), name='lode_issue_data'),

    ]
