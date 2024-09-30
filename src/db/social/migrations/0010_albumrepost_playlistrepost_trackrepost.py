# Generated by Django 5.1 on 2024-09-30 07:23

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_albumtrack_album_tracks_playlisttrack_and_more'),
        ('person', '0004_savedplaylist_person_saved_playlists_and_more'),
        ('social', '0009_alter_tracklike_owner_alter_playlistcomment_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumRepost',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='person.person', verbose_name='Owner')),
                ('target', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='music.album', verbose_name='Album')),
            ],
            options={
                'verbose_name': 'Album repost',
                'verbose_name_plural': 'Album reposts',
                'abstract': False,
                'constraints': [models.UniqueConstraint(fields=('owner', 'target'), name='unique_albumrepost')],
            },
        ),
        migrations.CreateModel(
            name='PlaylistRepost',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='person.person', verbose_name='Owner')),
                ('target', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='music.playlist', verbose_name='Playlist')),
            ],
            options={
                'verbose_name': 'Playlist repost',
                'verbose_name_plural': 'Playlist reposts',
                'abstract': False,
                'constraints': [models.UniqueConstraint(fields=('owner', 'target'), name='unique_playlistrepost')],
            },
        ),
        migrations.CreateModel(
            name='TrackRepost',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='person.person', verbose_name='Owner')),
                ('target', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='music.track', verbose_name='Track')),
            ],
            options={
                'verbose_name': 'Track repost',
                'verbose_name_plural': 'Track reposts',
                'abstract': False,
                'constraints': [models.UniqueConstraint(fields=('owner', 'target'), name='unique_trackrepost')],
            },
        ),
    ]
