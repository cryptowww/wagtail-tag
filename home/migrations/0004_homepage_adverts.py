# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 03:36
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_advert'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='adverts',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.Advert'),
        ),
    ]