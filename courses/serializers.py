from rest_framework import serializers
from .models import University,Program,Destination



class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model= University
        fields="__all__"



class ProgramSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    class Meta:
        model= Program
        fields="__all__"

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Destination
        fields="__all__"

