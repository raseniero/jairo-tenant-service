from django.shortcuts import render
from rest_framework import generics
from .models import Software
from .serializers import SoftwareSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "softwares": reverse("software-list", request=request, format=format),
        }
    )


class SoftwareListCreate(generics.ListCreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class SoftwareRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
