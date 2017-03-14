# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_aboutme_sitedes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u76f8\u518c\u540d\u79f0')),
                ('desc', models.TextField(max_length=200, verbose_name='\u76f8\u518c\u4ecb\u7ecd')),
                ('chick_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570')),
                ('zan_times', models.IntegerField(default=0, verbose_name='\u88ab\u8d5e\u6b21\u6570')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7f6e\u9876')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e')),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': '\u76f8\u518c\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, null=True, verbose_name='\u7167\u7247\u6807\u9898', blank=True)),
                ('desc', models.TextField(max_length=200, null=True, verbose_name='\u7167\u7247\u7b80\u4ecb', blank=True)),
                ('img', models.CharField(default=b'/static/tx/my.jpg', max_length=300, verbose_name='\u7167\u7247\u5730\u5740')),
                ('chick_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570')),
                ('zan_times', models.IntegerField(default=0, verbose_name='\u88ab\u8d5e\u6b21\u6570')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7f6e\u9876')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name_plural': '\u7167\u7247\u7ba1\u7406',
            },
        ),
    ]
