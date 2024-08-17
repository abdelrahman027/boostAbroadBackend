

from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer
# Create your views here.


@api_view(['GET'])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services,many=True)
    return Response({"services":serializer.data})
