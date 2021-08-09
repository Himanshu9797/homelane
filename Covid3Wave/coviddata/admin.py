from django.contrib import admin
from .models import CovidVaccineStatewise, StatewiseTestingDetails, Covid19cases

# Register your models here.
admin.site.register(CovidVaccineStatewise)
admin.site.register(StatewiseTestingDetails)
admin.site.register(Covid19cases)


