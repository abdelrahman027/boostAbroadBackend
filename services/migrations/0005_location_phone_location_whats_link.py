# Generated by Django 4.2.15 on 2024-08-31 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_event_knowledgehub'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='whats_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
