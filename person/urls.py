from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from person import views

urlpatterns = [
    path("persons/", views.PersonListCreate.as_view(), name="person-list"),
    path(
        "person/<int:pk>/",
        views.PersonRetriveUpdateDestroy.as_view(),
        name="person-detail",
    ),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
