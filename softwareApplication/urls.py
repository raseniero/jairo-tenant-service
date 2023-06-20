from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from softwareApplication import views

urlpatterns = [
    path("SoftwareApplication/", views.SoftwareApplicationListCreate.as_view(), name="softwareApplication-list"),
    path(
        "SoftwareApplication/<int:pk>/",
        views.SoftwareApplicationRetriveUpdateDestroy.as_view(),
        name="softwareApplication-detail",
    ),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
