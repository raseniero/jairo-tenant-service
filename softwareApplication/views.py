from django.shortcuts import render
from rest_framework import generics
from .models import SoftwareApplication
from .serializers import SoftwareApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "softwareApplications": reverse("softwareApplication-list", request=request, format=format),
        }
    )


class SoftwareApplicationListCreate(generics.ListCreateAPIView):
    queryset = SoftwareApplication.objects.all()
    serializer_class = SoftwareApplicationSerializer


class SoftwareApplicationRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoftwareApplication.objects.all()
    serializer_class = SoftwareApplicationSerializer
