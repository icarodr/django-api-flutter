from django.shortcuts import render
from flutterappdj.models import FlutterAppDj
from .serializers import FlutterAppDjSerializer
from rest_framework import viewsets

class FlutterAppDj(viewsets.ModelViewSet):
    queryset = FlutterAppDj.objects.all()
    serializer_class = FlutterAppDjSerializer
    