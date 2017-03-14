# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_album_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u76f8\u518c', blank=True, to='blog.Album', null=True),
        ),
    ]
