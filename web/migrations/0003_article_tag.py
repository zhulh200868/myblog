# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='web.Tag', blank=True),
        ),
    ]
