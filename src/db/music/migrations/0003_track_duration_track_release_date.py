# Generated by Django 5.1 on 2024-09-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='duration',
            field=models.DurationField(editable=False, null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='track',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Release date'),
        ),
    ]