# Generated by Django 5.1 on 2024-10-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_album_is_removed_albumtrack_is_removed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='albums_images', verbose_name='Image'),
        ),
    ]