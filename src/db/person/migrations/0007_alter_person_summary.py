# Generated by Django 5.1 on 2024-12-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_remove_person_is_removed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Summary'),
        ),
    ]
