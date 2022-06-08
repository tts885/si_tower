#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:43:22 2022

@author: guangdong.chen
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomUserCreationForm (SignupForm):
    Invitation_code = forms.CharField()
    
    class Meta:
        model =CustomUser
        # fields =('username','email','password1','password2','Invitation_code')

    def sigunp(self, request, user):
        user.Invitation_code = self.cleaned_data['Invitation_code']
        user.save()
        return user

