#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    :
# @File    : admin.py
# @Software: PyCharm


from django.contrib import admin
from blog_auth.models import User
from django.contrib.auth.admin import UserAdmin
from blog_auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class MyUserAdmin(UserAdmin):
    add_form=UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    # 修改用户信息
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password', 'email')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)
admin.site.register(User,MyUserAdmin)

