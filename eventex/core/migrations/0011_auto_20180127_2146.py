# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 21:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
