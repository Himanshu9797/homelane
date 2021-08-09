# Generated by Django 3.2.6 on 2021-08-08 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coviddata', '0002_auto_20210808_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='female',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='first_dose_administered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='male',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='second_dose_administered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='total_covaxin_administered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='total_coviShield_administered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='total_doses_administered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='total_sessions_conducted',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='total_sites',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinestatewise',
            name='transgender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
