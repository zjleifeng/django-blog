# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_album_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='img',
            field=models.CharField(default=b'/static/img/photo/default.jpg', max_length=300, verbose_name='\u7f29\u7565\u56fe'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.CharField(default='\u6e38\u5ba2', max_length=20, verbose_name='\u53d1\u9001\u8005'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.CharField(default=b'/static/photo/images/default.jpg', max_length=300, verbose_name='\u7167\u7247\u5730\u5740'),
        ),
    ]
