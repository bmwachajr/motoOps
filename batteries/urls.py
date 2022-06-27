from django.urls import path
from .views import BatteriesAPIView, BatteryAPIView

app_name = "batteries"

urlpatterns = [
    path('', BatteriesAPIView.as_view(),
        name='create'),
    path('<pk>', BatteryAPIView.as_view(),
        name='retrieve'),
]