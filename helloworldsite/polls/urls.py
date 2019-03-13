#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:45:40 2019

@author: kodtodya
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]