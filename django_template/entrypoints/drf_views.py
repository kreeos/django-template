from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request

from django.http import JsonResponse


class SampleView(APIView):
    def get(self, request: Request) -> JsonResponse:
        return JsonResponse(
            {'msg': "hello, world"}
        )
