# Generated by Django 5.1 on 2024-09-10 06:07

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_alter_album_owner_alter_playlist_owner_and_more'),
        ('social', '0004_alter_playlistcomment_owner_alter_playlistlike_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlistcomment',
            name='subject',
            field=models.TextField(null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='trackcomment',
            name='subject',
            field=models.TextField(null=True, verbose_name='Subject'),
        ),
        migrations.CreateModel(
            name='AlbumComment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.TextField(null=True, verbose_name='Subject')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='social.person', verbose_name='Owner')),
                ('target', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='music.album', verbose_name='Album')),
            ],
            options={
                'verbose_name': 'Album comment',
                'verbose_name_plural': 'Album comments',
                'abstract': False,
            },
        ),
    ]
