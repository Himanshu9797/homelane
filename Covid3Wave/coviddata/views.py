from django.views import View
from django.http import JsonResponse
import json
from django.core import serializers
from .models import CovidVaccineStatewise, StatewiseTestingDetails, Covid19cases
# Create your views here.

class DateInfo(View):
    def get(self, request, Date):

        vaccineStatewise = CovidVaccineStatewise.objects.filter(updated_on=Date)
        testingStatewise = StatewiseTestingDetails.objects.filter(date=Date)
        cases = Covid19cases.objects.filter(date=Date)

        data = {
            "vaccineStatewise": serializers.serialize('json', vaccineStatewise),
            "testingStatewise": serializers.serialize('json', testingStatewise),
            "cases": serializers.serialize('json', cases),
        }
        return JsonResponse(data, status=200)

