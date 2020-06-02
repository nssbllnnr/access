from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django.core.mail import send_mail
from .serializers import *
from rest_framework.response import Response

class PersonalViewSet(ModelViewSet):
    queryset = Employee.objects.all()
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

    def list(self, request, *args, **kwargs):

        page = self.paginate_queryset(self.get_queryset())

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(serializer.data)

class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # filter_backends = (OrderingFilter, SearchFilter)
    # ordering_fields = ['price', 'seoson']
    # search_fields = ['width', 'profile', 'diameter']

class AccessViewSet(ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    # filter_backends = (OrderingFilter, SearchFilter)
    # ordering_fields = ['price', 'seoson']
    # search_fields = ['width', 'profile', 'diameter']

class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    # filter_backends = (OrderingFilter, SearchFilter)
    # ordering_fields = ['price', 'seoson']
    # search_fields = ['width', 'profile', 'diameter']