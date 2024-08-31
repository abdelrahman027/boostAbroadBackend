# Generated by Django 4.2.15 on 2024-08-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('address', models.CharField(max_length=512)),
                ('description', models.TextField(max_length=3000)),
                ('event_image', models.ImageField(blank=True, default='events/event1.jpg', null=True, upload_to='events/')),
            ],
        ),
        migrations.CreateModel(
            name='knowledgehub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('address', models.CharField(max_length=512)),
                ('description', models.TextField(max_length=3000)),
                ('knowledge_image', models.ImageField(blank=True, default='knowledge/knowledge1.jpg', null=True, upload_to='knowledge/')),
            ],
        ),
    ]
