from django.shortcuts import render

# -------------MODELOS--------------
from ejemplo.models import Profile

# ------------SERIALIZERS-----------
from ejemplo.serializer import EjemploSerializer
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

class ProfileList(APIView):
    def get(self, request, format=None):
        queryset = Profile.objects.filter(delete=False)
        serializer = EjemploSerializer(queryset, many=True)
        return Response(serializer.data)