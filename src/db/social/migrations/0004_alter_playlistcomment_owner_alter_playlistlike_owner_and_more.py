# Generated by Django 5.1 on 2024-09-09 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_playlistcomment_owner_playlistlike_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistcomment',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='social.person', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='playlistlike',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='social.person', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='trackcomment',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='social.person', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='tracklike',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.RESTRICT, to='social.person', verbose_name='Owner'),
        ),
    ]
