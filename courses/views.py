

from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import University
from .serializers import UniversitySerializer
# Create your views here.


@api_view(['GET'])
def get_all_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities,many=True)
    return Response({"Universities":serializer.data})
