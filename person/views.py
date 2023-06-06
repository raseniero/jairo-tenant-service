from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "persons": reverse("user-list", request=request, format=format),
        }
    )


class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
