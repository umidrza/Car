from django.urls import path
from .views import *

app_name = 'car'

urlpatterns = [
    path('', cars_list, name='cars-list'),
    path('<int:id>/', car_detail, name='car-detail'),
    path('owners/', owner_list, name='owners-list'),
]
