# Generated by Django 3.1.2 on 2021-01-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightSafetyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_time', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]
