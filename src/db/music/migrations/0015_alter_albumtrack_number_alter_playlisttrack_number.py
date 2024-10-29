# Generated by Django 5.1 on 2024-10-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_alter_albumtrack_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumtrack',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Number in the list'),
        ),
        migrations.AlterField(
            model_name='playlisttrack',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Number in the list'),
        ),
    ]