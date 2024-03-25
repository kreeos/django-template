from django.urls import path
from .entrypoints import drf_views

urlpatterns = [
    path("sample/<int:pk>", drf_views.SampleView.as_view())
]
