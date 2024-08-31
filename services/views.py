

from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service,Location,Event,knowledgehub
from .serializers import ServiceSerializer,LocationSerializer,EventSerializer,KnowledgeSerializer
# Create your views here.


@api_view(['GET'])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services,many=True)
    return Response({"services":serializer.data})


@api_view(['GET'])
def get_all_locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations,many=True)
    return Response({"locations":serializer.data})


@api_view(['GET'])
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events,many=True)
    return Response({"events":serializer.data})


@api_view(['GET'])
def get_event_detail(request,pk):
    event=get_object_or_404(Event ,id=pk)
    serializer =EventSerializer(event,many=False)
    return Response({"event":serializer.data})


@api_view(['GET'])
def get_all_knowledges(request):
    knowledges = knowledgehub.objects.all()
    serializer = KnowledgeSerializer(knowledges,many=True)
    return Response({"knowledges":serializer.data})


@api_view(['GET'])
def get_knowledge_detail(request,pk):
    knowledge=get_object_or_404(knowledgehub ,id=pk)
    serializer =KnowledgeSerializer(knowledge,many=False)
    return Response({"knowledge":serializer.data})
