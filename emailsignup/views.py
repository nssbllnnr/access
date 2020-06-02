from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import *
from .functions import email_client

@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    print(request)
    return Response("Email account is activated")


class FeedbackList(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email_client(request)
        return Response({
            'resultCode' : 0,
            'messages' : ['Email sent'],
            'data' : []
        })