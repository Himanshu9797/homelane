# Generated by Django 3.2.6 on 2021-08-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coviddata', '0003_auto_20210808_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatewiseTestingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('totalsamples', models.CharField(blank=True, max_length=255, null=True)),
                ('negative', models.CharField(blank=True, max_length=255, null=True)),
                ('positive', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]