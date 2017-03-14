# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_album_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tags',
        ),
    ]
