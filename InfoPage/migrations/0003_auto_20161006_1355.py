# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InfoPage', '0002_student_names'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_names',
            new_name='student_name',
        ),
    ]