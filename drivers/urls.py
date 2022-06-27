from django.urls import path
from .views import DriversAPIView, DriverAPIView

app_name = "drivers"

urlpatterns = [
    path('', DriversAPIView.as_view(),
        name='create'),
    path('<pk>', DriverAPIView.as_view(),
        name='retrieve'),
]