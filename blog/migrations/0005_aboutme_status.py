# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170313_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')]),
        ),
    ]
