from django.urls import path
from .views import StationsAPIView, StationAPIView

app_name = "stations"

urlpatterns = [
    path('', StationsAPIView.as_view(),
        name='create'),
    path('<pk>', StationAPIView.as_view(),
        name='retrieve'),
]