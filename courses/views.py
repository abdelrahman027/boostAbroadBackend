

from django.shortcuts import get_object_or_404, render
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import University,Program,Destination
from .serializers import UniversitySerializer,ProgramSerializer,DestinationSerializer
# Create your views here.


@api_view(['GET'])
def get_all_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities,many=True)
    return Response({"universities":serializer.data})


@api_view(['GET'])
def get_all_programs(request):
    programs = Program.objects.all()
    serializer = ProgramSerializer(programs,many=True)
    return Response({"programs":serializer.data})


@api_view(['GET'])
def get_programs_detail(request,pk):
    program=get_object_or_404(Program ,id=pk)
    serializer =ProgramSerializer(program,many=False)
    return Response({"program":serializer.data})

@api_view(['GET'])
def get_university_detail(request,pk):
    university=get_object_or_404(University ,id=pk)
    serializer =UniversitySerializer(university,many=False)
    return Response({"university":serializer.data})

#dest
@api_view(['GET'])
def get_all_destinations(request):
    destinations= Destination.objects.all()
    serializer = DestinationSerializer(destinations,many=True)
    return Response({"destinations":serializer.data})


@api_view(['GET'])
def get_destination_detail(request,pk):
    destination=get_object_or_404(Destination ,id=pk)
    serializer =DestinationSerializer(destination,many=False)
    return Response({"destination":serializer.data})
