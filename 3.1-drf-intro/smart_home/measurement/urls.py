from django.urls import path
from .views import GetSensors, GetSensor, CreateSensor, UpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/create', CreateSensor.as_view()),
    path('sensors/', GetSensors.as_view()),
    path('sensors/<pk>', GetSensor.as_view()),
    path('sensors/update/<pk>', UpdateSensor.as_view()),
    path('measurement/create', CreateMeasurement.as_view())
]
