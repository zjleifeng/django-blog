# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userinfo',
            field=models.TextField(null=True, verbose_name='\u4e2a\u4eba\u4ecb\u7ecd', blank=True),
        ),
    ]
