from django.db import models

# Create your models here.

class CovidVaccineStatewise(models.Model):
	updated_on = models.DateField(null=True, blank=True)
	state = models.CharField(max_length=100,null=True, blank=True)
	total_doses_administered = models.CharField(max_length = 255, null=True, blank=True)
	total_sessions_conducted = models.CharField(max_length = 255, null=True, blank=True)
	total_sites = models.CharField(max_length = 255, null=True, blank=True)
	first_dose_administered = models.CharField(max_length = 255, null=True, blank=True)
	second_dose_administered = models.CharField(max_length = 255, null=True, blank=True)
	male = models.CharField(max_length = 255, null=True, blank=True)
	female = models.CharField(max_length = 255, null=True, blank=True)
	transgender = models.CharField(max_length = 255, null=True, blank=True)
	total_covaxin_administered = models.CharField(max_length = 255, null=True, blank=True)
	total_coviShield_administered = models.CharField(max_length = 255, null=True, blank=True)
	total_sputnikV_administered = models.CharField(max_length = 255, null=True, blank=True)
	aefi = models.CharField(max_length = 255, null=True, blank=True)
	age18to45 = models.CharField(max_length = 255, null=True, blank=True)
	age45to60 = models.CharField(max_length = 255, null=True, blank=True)
	above60 = models.CharField(max_length = 255, null=True, blank=True)
	total_vaccinated = models.CharField(max_length = 255, null=True, blank=True)


class StatewiseTestingDetails(models.Model):
	date = models.DateField(null=True, blank=True)
	state = models.CharField(max_length=100,null=True, blank=True)
	totalsamples = models.CharField(max_length = 255, null=True, blank=True)
	negative = models.CharField(max_length = 255, null=True, blank=True)
	positive = models.CharField(max_length = 255, null=True, blank=True)


class Covid19cases(models.Model):
	date = models.DateField(null=True, blank=True)
	time = models.CharField(max_length=20,null=True, blank=True)
	state = models.CharField(max_length=100,null=True, blank=True)
	confirmedIndianNational = models.CharField(max_length=255,null=True, blank=True)
	confirmedForeignNational = models.CharField(max_length=255,null=True, blank=True)
	cured = models.CharField(max_length=255,null=True, blank=True)
	deaths = models.CharField(max_length=255,null=True, blank=True)
	confirmed = models.CharField(max_length=255,null=True, blank=True)





