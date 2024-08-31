from rest_framework import serializers
from .models import Service,Location,knowledgehub,Event

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Service
        fields="__all__"


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Location
        fields="__all__"



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model= Event
        fields="__all__"


class KnowledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model= knowledgehub
        fields="__all__"