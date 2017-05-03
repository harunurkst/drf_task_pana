# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('districts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Districts')),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Divisions'),
        ),
    ]