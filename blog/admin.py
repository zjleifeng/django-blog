#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    :
# @File    : admin.py
# @Software: PyCharm


from django.contrib import admin
from blog.models import Article,Tag, Category, Comment, Links, Advert,Notification,Aboutme

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', 'create_time')
    list_display = ('name', )
    #fields = ('__all__',)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', 'parent','rank','create_time')
    list_display = ('name', 'parent', 'rank', 'create_time')
    #fields = ('__all__',)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author','tags','category')
    list_filter = ('title', 'desc', 'content',
                   'img', 'category', 'tags','author','chick_count','zan_times','is_top','rank','status')
    list_display = ('title', 'category', 'author',
                    'status', 'is_top')
    fieldsets = (
        (u'基本信息', {
            'fields': ('title', 'img',
                       'category', 'tags', 'author',
                       'is_top', 'rank', 'status')
            }),
        (u'内容', {
            'fields': ('content',)
            }),
        (u'摘要', {
            'fields': ('desc',)
            }),

        (u'高级设置', {
            'classes':('collapse',),
            'fields': ('chick_count','zan_times',)
        }),
    )




class CommentAdmin(admin.ModelAdmin):
    search_fields = ('article','status')
    list_filter = ('article', 'status')
    list_display = ('content', 'username','email', 'siteurl', 'article','parent','status','create_time')
    #fields = ('__all__',)

#注册导航条
class LinksAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'siteurl', 'status', 'create_time')
    list_filter = ('name', 'status')
    #fields = ('__all__',)


class AdvertAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'des', 'image_url','callback_url')
    list_filter = ('title',)
    #fields = ('title','des','image_url','callback_url',)


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('title', 'from_user', 'to_user', 'create_time')
    list_filter = ('create_time',)
    fields = ('title', 'is_read', 'text',
              'url', 'from_user', 'to_user', 'type')

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Aboutme)