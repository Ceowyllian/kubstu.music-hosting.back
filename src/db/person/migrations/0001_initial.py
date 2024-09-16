# Generated by Django 5.1 on 2024-09-16 07:21

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0007_alter_album_owner_alter_playlist_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar')),
                ('summary', models.CharField(blank=True, null=True, verbose_name='Summary')),
                ('public_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Public email')),
                ('saved_playlists', models.ManyToManyField(related_name='followers', related_query_name='follower', to='music.playlist')),
                ('subscribers', models.ManyToManyField(related_query_name='subscriber', to='person.person')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]
