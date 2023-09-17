# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorWithMeasurementSerializer

class GetSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class GetSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorWithMeasurementSerializer

#Изменить датчик. Указываются название и описание.
#Добавить измерение. Указываются ID датчика и температура.

class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer