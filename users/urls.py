from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path("users/", views.UserViewSet.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetailViewSet.as_view(), name="user-detail"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
