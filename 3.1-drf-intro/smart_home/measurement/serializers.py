from rest_framework import serializers
from .models import Measurement, Sensor
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'date', 'image']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorWithMeasurementSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']