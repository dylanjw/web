# Generated by Django 2.1.2 on 2018-11-13 16:41

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0036_auto_20180917_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscriber',
            name='github',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='emailsubscriber',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='emailsubscriber',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_subscriptions', to='dashboard.Profile'),
        ),
    ]
