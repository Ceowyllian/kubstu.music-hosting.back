# Generated by Django 5.1 on 2024-09-27 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_alter_album_owner_alter_playlist_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tracks',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='tracks',
        ),
    ]