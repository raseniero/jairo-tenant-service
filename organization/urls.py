from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = [
    path(
        "organizations/",
        views.OrganizationListCreate.as_view(),
        name="organization-list",
    ),
    path(
        "organization/<int:pk>/",
        views.OrganizationRetrieveUpdateDestroy.as_view(),
        name="organization-detail",
    ),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
