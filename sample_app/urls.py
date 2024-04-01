from django.urls import path
from .entrypoints import drf_views

urlpatterns = [
    path("sample/<int:pk>", drf_views.SampleViewDetail.as_view()),
    path("sample", drf_views.SampleViewList.as_view())
]
