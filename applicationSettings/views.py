from django.shortcuts import render
from rest_framework import generics
from .models import Application
from .serializers import ApplicationSettingsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "applicationSettings": reverse("applicationSettings-list", request=request, format=format),
        }
    )


class ApplicationSettingsListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSettingsSerializer


class ApplicationSettingsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSettingsSerializer