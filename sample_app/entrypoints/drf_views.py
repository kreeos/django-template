from django.http import JsonResponse, HttpRequest
from django.views import View
from rest_framework import request

from sample_app.adapter.repo import DjangoSampleRepository
from sample_app.service.dto import SampleDTO
from sample_app.service.usecase import SampleUsecase

import json

class SampleViewList(View):
    def post(self, request: request.Request) -> JsonResponse:
        repo = DjangoSampleRepository()
        usecase = SampleUsecase(repo)
        model = usecase.create(json.loads(request.body).get('text'))
        return JsonResponse(data=SampleDTO.from_model(model).to_dict())

class SampleViewDetail(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        repo = DjangoSampleRepository()
        usecase = SampleUsecase(repo)
        try:
            model = usecase.get(pk)
        except ValueError as e:
            return JsonResponse({'message': 'Sample Model Not Found'}, status=404)
        return JsonResponse(data=SampleDTO.from_model(model).to_dict())

