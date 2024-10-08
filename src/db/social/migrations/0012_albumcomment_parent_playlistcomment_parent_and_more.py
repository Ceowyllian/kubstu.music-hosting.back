# Generated by Django 5.1 on 2024-10-02 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_albumcomment_is_removed_albumlike_is_removed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='children', to='social.albumcomment'),
        ),
        migrations.AddField(
            model_name='playlistcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='children', to='social.playlistcomment'),
        ),
        migrations.AddField(
            model_name='trackcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='children', to='social.trackcomment'),
        ),
    ]
