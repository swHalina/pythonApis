from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer