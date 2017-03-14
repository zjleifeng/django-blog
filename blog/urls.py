#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-6 下午12:18
# @Author  : eric
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import include, url
from django.contrib import admin
from blog.views import IndexView,ArticleView,AllView,PostCommentView,SearchView,CaregoryView,TagsView,DateArticleView,AboutMeView,MsgBookView,PhotoView,PhothListView
from myblog import settings
from django.views.generic import TemplateView, DetailView

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index_view'),
    url(r'^forgetpassword/$',
            TemplateView.as_view(template_name="sys/forgetpassword.html"),
            name='forgetpassword-view'),
    url(r'^resetpassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            TemplateView.as_view(template_name="sys/resetpassword.html"),
            name='resetpassword-view'),
    url(r'^aboutme/$',AboutMeView.as_view(),
            name='aboutme-view'),
    url(r'^media/article/(?P<path>.*)', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT+'/article'}),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name='article-view'),
    url(r'^tag/(?P<tag_name>.+)/$', TagsView.as_view(), name='tag-view'),
    url(r'^all/$', AllView.as_view(), name='all-view'),
    url(r'^comment/(?P<slug>\w+)/$',PostCommentView.as_view(),name='postcomment-view'),
    url(r'^search/$',SearchView.as_view(),name='search-view'),
    url(r'^category/(?P<pk>\w+)/$',CaregoryView.as_view(),name='category-view'),
    url(r'^datearticle/(?P<year>\d+)/(?P<month>\d+)/$', DateArticleView.as_view(), name='datearticle-view'),
    url(r'^msgbook/$',MsgBookView.as_view(),name='msgbook-view'),
    url(r'^photo/$',PhotoView.as_view(),name='photo-view'),
    url(r'^photolist/(?P<pk>\d+)/$', PhothListView.as_view(), name='photolist-view'),
]
