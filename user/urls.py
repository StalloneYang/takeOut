#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 17:48
# @Author  : StalloneYang
# @File    : urls.py
# @desc:

from  django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^uname_exist/$',views.uname_exist),
    url(r'^info/$',views.info),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
]

