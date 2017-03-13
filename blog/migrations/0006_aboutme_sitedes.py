# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_aboutme_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='sitedes',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name='\u7ad9\u70b9\u7b80\u4ecb'),
        ),
    ]
