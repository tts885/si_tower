#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:40:56 2022
@author: guangdong.chen
"""

from django.urls import path
from . import views
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    # ログイン用のテンプレート(フォーム)をレンダリング
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    ]
