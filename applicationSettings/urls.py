from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from applicationSettings import views

urlpatterns = [
    path("applicationSettings/", views.ApplicationSettingsListCreate.as_view(), name="applicationSettings-list"),
    path(
        "applicationSettings/<int:pk>/",
        views.ApplicationSettingsRetriveUpdateDestroy.as_view(),
        name="applicationSettings-detail",
    ),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
