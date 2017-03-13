# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20170308_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('nickname', models.CharField(max_length=30, verbose_name='\u6635\u79f0')),
                ('sitename', models.CharField(max_length=30, verbose_name='\u4e2a\u4eba\u7f51\u7ad9\u540d\u79f0')),
                ('siteurl', models.URLField(verbose_name='\u4e2a\u4eba\u7f51\u7ad9\u5730\u5740')),
                ('content', models.TextField(max_length=2000, verbose_name='\u4e2a\u4eba\u81ea\u6211\u4ecb\u7ecd')),
                ('uselan', models.CharField(max_length=100, verbose_name='\u7a0b\u5e8f\u8bed\u8a00')),
            ],
            options={
                'verbose_name_plural': '\u81ea\u6211\u4ecb\u7ecd',
            },
        ),
        migrations.CreateModel(
            name='MsgBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('content', models.TextField(verbose_name='\u7559\u8a00\u5185\u5bb9')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='\u90ae\u7bb1\u5730\u5740', blank=True)),
                ('siteurl', models.URLField(max_length=50, null=True, verbose_name='\u4e2a\u4eba\u7f51\u7ad9\u5730\u5740', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('authuser', models.ForeignKey(verbose_name='\u4f5c\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(verbose_name='\u7236\u7ea7\u7559\u8a00', blank=True, to='blog.MsgBook', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name_plural': '\u7559\u8a00',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('text', models.TextField(verbose_name='\u5185\u5bb9')),
                ('url', models.CharField(max_length=200, null=True, verbose_name='\u8fde\u63a5', blank=True)),
                ('type', models.CharField(max_length=20, null=True, verbose_name='\u7c7b\u578b', blank=True)),
                ('is_read', models.IntegerField(default=0, verbose_name='\u662f\u5426\u8bfb\u8fc7', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('from_user', models.ForeignKey(related_name='from_user_notification_set', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u53d1\u9001\u8005')),
                ('to_user', models.ForeignKey(related_name='to_user_notification_set', verbose_name='\u63a5\u6536\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u6d88\u606f',
                'verbose_name_plural': '\u6d88\u606f',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=blog.models.Tag, max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
    ]
