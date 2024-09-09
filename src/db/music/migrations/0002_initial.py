# Generated by Django 5.1 on 2024-09-09 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, related_name='created_playlists', related_query_name='created_playlist', to='social.person', verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='track',
            name='uploaded_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, related_name='uploaded_tracks', related_query_name='uploaded_track', to='social.person', verbose_name='Uploaded by'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(related_name='playlists', to='music.track', verbose_name='Tracks'),
        ),
    ]