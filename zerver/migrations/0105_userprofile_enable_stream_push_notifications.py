# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0104_fix_unreads'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='enable_stream_push_notifications',
            field=models.BooleanField(default=False),
        ),
    ]
