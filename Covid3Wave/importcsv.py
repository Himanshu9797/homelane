
import csv
import os
from coviddata.models import CovidVaccineStatewise, StatewiseTestingDetails, Covid19cases # imports the model
with open('covid_vaccine_statewise.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            p = CovidVaccineStatewise(updated_on=row['Updated On'], state=row['State'], 
            	total_doses_administered=row['Total Doses Administered'],total_sessions_conducted=row['Total Sessions Conducted']
            	,total_sites=row['Total Sites '],first_dose_administered=row['First Dose Administered']
            	,second_dose_administered=row['Second Dose Administered'],male=row['Male(Individuals Vaccinated)'],
            	female=row['Female(Individuals Vaccinated)'], transgender=row['Transgender(Individuals Vaccinated)']
            	,total_covaxin_administered=row['Total Covaxin Administered'], total_coviShield_administered=row['Total CoviShield Administered']
            	,total_sputnikV_administered = row['Total Sputnik V Administered'], aefi = row['AEFI']
            	,age18to45 = row['18-45 years (Age)'], age45to60 = row['45-60 years (Age)'], above60 = row['60+ years (Age)']
            	,total_vaccinated=row['Total Individuals Vaccinated'])
            p.save()

with open('StatewiseTestingDetails.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            p = StatewiseTestingDetails(date=row['Date'], state=row['State'], 
            	totalsamples=row['TotalSamples'],negative=row['Negative']
            	,positive=row['Positive'],)
            p.save()


with open('covid_19_india.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            p = Covid19cases(date=row['Date'], time=row['Time'], 
            	state=row['State/UnionTerritory'],confirmedIndianNational=row['ConfirmedIndianNational']
            	,confirmedForeignNational=row['ConfirmedForeignNational'], cured=row['Cured'],
            	deaths=row['Deaths'], confirmed = row['Confirmed'])
            p.save()
