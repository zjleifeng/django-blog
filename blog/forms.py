#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from blog.models import Article
class AddArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = (
        'title', 'desc', 'content', 'img', 'category', 'tags', 'author', 'is_top','rank','chick_count', 'zan_times','status')
        widgets = {


        }

