#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:40:56 2022
@author: guangdong.chen
"""

from django.urls import path
from . import views
from allauth.account.views import LoginView, LogoutView, PasswordResetView, password_reset_from_key,SignupView
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [

    # ログイン用のテンプレート(フォーム)をレンダリング
    path('', LoginView.as_view(template_name='allauth/account/login.html'), name='login'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/', SignupView.as_view(template_name = 'allauth/account/signup.html'), name='signup'),

    path('passwordReset/', PasswordResetView.as_view(template_name='allauth/account/password_reset.html'), name='passwordReset'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    ]
