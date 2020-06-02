from rest_framework.serializers import ModelSerializer
from .models import *

class PersonalSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['student_id','name','surname','deportment','position','check_in','check_out']

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['student_id','image','name','surname','check_in','check_out']

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_ip','serial_number','device_model','is_out','wait_time','last_activity']

class AccessSerializer(ModelSerializer):
    class Meta:
        model = Access
        fields = ['card_id','access','user','registred_date']

class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ['entry_date','out_date','card','device']