#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    :
# @File    : models.py
# @Software: PyCharm

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tximg=models.CharField(max_length=200,default='/static/tx/default.jpg',verbose_name=u'头像地址')
    userinfo=models.TextField(max_length=200,blank=True,null=True,verbose_name=u'个人介绍')
    qq=models.CharField(max_length=20,blank=True,null=True,verbose_name=u'QQ号码')
    mobile=models.CharField(max_length=11,blank=True,null=True,unique=True,verbose_name=u'手机号码')
    siteurl=models.URLField(max_length=100,blank=True,null=True,verbose_name=u'个人网站地址')

    class Meta:
        verbose_name_plural=u'用户管理'
        ordering=['-id']

    def __unicode__(self):
        return self.username
    __str__=__unicode__



