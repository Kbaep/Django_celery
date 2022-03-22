from django.urls import path, include
from .views import ProfileCreateAPI,ProfileDetailAPI

urlpatterns = [
    path('profile/create', ProfileCreateAPI.as_view()),
    path('profile/<int:pk>', ProfileDetailAPI.as_view())
]