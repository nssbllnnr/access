from rest_framework.serializers import ModelSerializer
from .models import *

class PersonalSerializer(ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'