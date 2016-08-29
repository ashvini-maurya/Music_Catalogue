# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-29 20:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gaana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='login',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gaana.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='gaana.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_year',
            field=models.DateTimeField(default=2016),
        ),
        migrations.AddField(
            model_name='like',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Song'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]