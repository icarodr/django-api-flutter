from dataclasses import field
from rest_framework import serializers
from .models import FlutterAppDj

class FlutterAppDjSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlutterAppDj
        fields = [
            'nome',
            'email'
        ]