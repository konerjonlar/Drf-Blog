from django.urls import path

from accounts.api.views import UserCreateAPIView, UserDetailAPIView, UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("signup/", UserCreateAPIView.as_view(), name="user-signup"),
]
