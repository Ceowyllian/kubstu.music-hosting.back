# Generated by Django 5.1 on 2024-09-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_track_duration_track_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(editable=False, verbose_name='Duration'),
        ),
    ]