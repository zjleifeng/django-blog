#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-3 下午3:55
# @Author  : eric
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from blog_auth.views import UserControl
from django.conf.urls import url



urlpatterns = [
        url(r'^usercontrol/(?P<slug>\w+)$', UserControl.as_view()),
]


