# Generated by Django 4.2.15 on 2024-08-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_program_requirement1_program_requirement2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('country', models.CharField(default='UK', max_length=50)),
                ('city', models.CharField(default='London', max_length=50)),
                ('continent', models.CharField(default='Europe', max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='destinations/athens.png', null=True, upload_to='destinations/')),
            ],
        ),
    ]
