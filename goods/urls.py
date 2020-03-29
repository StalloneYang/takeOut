#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :  2020/3/25 0:12
# @Author  :  StalloneYang
# @File    :  urls.py
# @desc:

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$',views.detail),


]

