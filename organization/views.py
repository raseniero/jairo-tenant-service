from .models import Organization
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import OrganizationSerializer

# Create your views here.


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "organizations": reverse(
                "organization-list", request=request, format=format
            ),
        }
    )


class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
