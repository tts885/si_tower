#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:43:22 2022

@author: guangdong.chen
"""
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm (UserCreationForm):
    
    class Meta:
        model =CustomUser
        fields =('username','email','password1','password2','Invitation_code')

