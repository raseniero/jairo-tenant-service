from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from softwareApplication import views

urlpatterns = [
    path("SoftwareApplication/", views.SoftwareListCreate.as_view(), name="software-list"),
    path(
        "SoftwareApplication/<int:pk>/",
        views.SoftwareRetriveUpdateDestroy.as_view(),
        name="software-detail",
    ),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
