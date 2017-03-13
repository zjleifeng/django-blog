# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_auth', '0002_user_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userinfo',
            field=models.TextField(max_length=200, null=True, verbose_name='\u4e2a\u4eba\u4ecb\u7ecd', blank=True),
        ),
    ]
