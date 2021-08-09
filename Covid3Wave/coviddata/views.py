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


class StateInfo(View):
    def get(self, request, state):

        vaccineStatewise = CovidVaccineStatewise.objects.filter(state=state).order_by('updated_on')
        testingStatewise = StatewiseTestingDetails.objects.filter(state=state).order_by('date')
        cases = Covid19cases.objects.filter(state=state).order_by('date')

        data = {
            "vaccineStatewise": serializers.serialize('json', vaccineStatewise),
            "testingStatewise": serializers.serialize('json', testingStatewise),
            "cases": serializers.serialize('json', cases),
        }
        return JsonResponse(data, status=200)

class PinpointState(View):
    def get(self, request, *args, **kwargs):
        vaccineStatewise = CovidVaccineStatewise.objects.filter(state=kwargs['state'], updated_on=kwargs['Date']).order_by('updated_on')
        testingStatewise = StatewiseTestingDetails.objects.filter(state=kwargs['state'], date=kwargs['Date']).order_by('date')
        cases = Covid19cases.objects.filter(state=kwargs['state'], date=kwargs['Date']).order_by('date')

        data = {
            "vaccineStatewise": serializers.serialize('json', vaccineStatewise),
            "testingStatewise": serializers.serialize('json', testingStatewise),
            "cases": serializers.serialize('json', cases),
        }
        return JsonResponse(data, status=200)

class PinpointInfo(View):
    def get(self, request, *args, **kwargs):

        vaccineStatewise = CovidVaccineStatewise.objects.filter(state__in=kwargs['state'].split(","), updated_on=kwargs['Date']).order_by('updated_on')
        testingStatewise = StatewiseTestingDetails.objects.filter(state__in=kwargs['state'].split(","), date=kwargs['Date']).order_by('date')
        cases = Covid19cases.objects.filter(state__in=kwargs['state'].split(","), date=kwargs['Date']).order_by('date')

        data = {
            "vaccineStatewise": serializers.serialize('json', vaccineStatewise),
            "testingStatewise": serializers.serialize('json', testingStatewise),
            "cases": serializers.serialize('json', cases),
        }
        return JsonResponse(data, status=200)
