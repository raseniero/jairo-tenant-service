from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path("users/", views.UserViewSet.as_view(), name="user-list"),
    path("user/<int:pk>/", views.UserDetailViewSet.as_view(), name="user-detail"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
