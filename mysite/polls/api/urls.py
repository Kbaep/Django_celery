from django.urls import path, include

urlpatterns = [
    path('v1/', include('polls.api.v1.urls'))
]
