from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django.core.mail import send_mail
from .serializers import *

class PersonalViewSet(ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['name', 'surname']
    search_fields = ['name', 'surname', 'student_id']

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['name', 'surname']
    search_fields = ['name', 'surname', 'student_id']

class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # filter_backends = (OrderingFilter, SearchFilter)
    # ordering_fields = ['price', 'seoson']
    # search_fields = ['width', 'profile', 'diameter']
