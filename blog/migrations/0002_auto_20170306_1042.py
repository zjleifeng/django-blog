# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='authuser',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(verbose_name='\u7236\u7ea7\u8bc4\u8bba', blank=True, to='blog.Comment', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='blog.Category', null=True, verbose_name='\u4e0a\u7ea7\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u5206\u7c7b', blank=True, to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
