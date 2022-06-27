from django.urls import path
from .views import SwapsAPIView, SwapAPIView

app_name = "swaps"

urlpatterns = [
    path('', SwapsAPIView.as_view(),
        name='create'),
    path('<pk>', SwapAPIView.as_view(),
        name='retrieve'),
]