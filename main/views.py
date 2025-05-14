from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import TestSerializer, ResultSerializer


class TestListApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TestSerializer


class TestDetailApiView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    permission_classes = [AllowAny]
    serializer_class = TestSerializer
    lookup_field = 'pk'


class ResultCreateApiView(generics.CreateAPIView):
    queryset = Result.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer

