# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u5e7f\u544a\u6807\u9898')),
                ('des', models.TextField(max_length=300, verbose_name='\u5e7f\u544a\u63cf\u8ff0')),
                ('image_url', models.ImageField(upload_to=b'uploads/ad/%Y/%m', verbose_name='\u5e7f\u544a\u56fe\u7247')),
                ('callback_url', models.URLField(null=True, verbose_name='\u56de\u8c03URL', blank=True)),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': '\u5e7f\u544a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('desc', models.CharField(max_length=100, null=True, verbose_name='\u6587\u7ae0\u63cf\u8ff0', blank=True)),
                ('content', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('img', models.ImageField(upload_to=b'uploads/article', null=True, verbose_name='\u7f29\u7565\u56fe', blank=True)),
                ('chick_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570')),
                ('zan_times', models.IntegerField(default=0, verbose_name='\u88ab\u8d5e\u6b21\u6570')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7f6e\u9876')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
            ],
            options={
                'ordering': ['rank', '-is_top', '-create_time'],
                'verbose_name_plural': '\u6587\u7ae0\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name_plural': '\u5206\u7c7b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('username', models.CharField(max_length=30, null=True, verbose_name='\u7528\u6237\u540d', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='\u90ae\u7bb1\u5730\u5740', blank=True)),
                ('siteurl', models.URLField(max_length=50, null=True, verbose_name='\u4e2a\u4eba\u7f51\u7ad9\u5730\u5740', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u6240\u5c5e\u6587\u7ae0', blank=True, to='blog.Article', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name_plural': '\u8bc4\u8bba\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u94fe\u63a5\u540d\u79f0')),
                ('des', models.CharField(max_length=200, verbose_name='\u94fe\u63a5\u8bf4\u660e')),
                ('siteurl', models.URLField(verbose_name='\u94fe\u63a5\u5730\u5740')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u6807\u7b7e\u7ba1\u7406',
            },
        ),
    ]
