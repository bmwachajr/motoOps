from django.urls import path
from .views import BatteriesAPIView, BatteryAPIView, BatteryTelematicsAPIView

app_name = "batteries"

urlpatterns = [
    path('', BatteriesAPIView.as_view(),
        name='create'),
    path('<pk>', BatteryAPIView.as_view(),
        name='retrieve'),
    path('<pk>/telematics', BatteryTelematicsAPIView.as_view(),
        name='create'),
]