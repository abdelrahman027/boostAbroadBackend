# Generated by Django 4.2.15 on 2024-08-19 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_university_city_university_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('given_degree', models.CharField(max_length=100)),
                ('duration_from', models.IntegerField()),
                ('duration_to', models.IntegerField()),
                ('first_sem_date', models.CharField(max_length=100)),
                ('second_sem_date', models.CharField(max_length=100)),
                ('fees', models.CharField(max_length=50)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.university')),
            ],
        ),
    ]
