from django.urls import path
from .views import DateInfo

urlpatterns = [
    path('Get_date_info(<Date>)/', DateInfo.as_view()),
]