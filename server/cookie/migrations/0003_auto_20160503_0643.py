# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0002_cookie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie',
            old_name='cookie',
            new_name='chrome_cookie',
        ),
        migrations.RemoveField(
            model_name='cookie',
            name='browser',
        ),
        migrations.AddField(
            model_name='cookie',
            name='firefox_cookie',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]