from django.urls import path
from .views import DateInfo,StateInfo,PinpointState,PinpointInfo

urlpatterns = [
    path('Get_date_info(<Date>)/', DateInfo.as_view()),
    path('Get_state_info(<state>)/', StateInfo.as_view()),
    path('Pinpoint_state(<state>,<Date>)/', PinpointState.as_view()),
    path('Pinpoint_info(<Date>,<state>)/', PinpointInfo.as_view())
]