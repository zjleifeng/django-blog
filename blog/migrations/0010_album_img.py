# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_photo_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='img',
            field=models.CharField(default=b'/static/photo/default.jpg', max_length=300, verbose_name='\u7f29\u7565\u56fe'),
        ),
    ]
