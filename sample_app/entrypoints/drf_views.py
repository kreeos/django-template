from rest_framework.views import APIView
from rest_framework.request import Request

from django.http import JsonResponse

from sample_app.adapter.repo import DjangoSampleRepository
from sample_app.service.usecase import SampleUsecase


class SampleView(APIView):
    def get(self, request: Request, pk: int) -> JsonResponse:
        repo = DjangoSampleRepository()
        usecase = SampleUsecase(repo)
        model = usecase.get(pk)
        if not model:
            return JsonResponse({'message': 'Not Found'}, status=404)
        return model

    def post(self, request: Request) -> JsonResponse:
        repo = DjangoSampleRepository()
        usecase = SampleUsecase(repo)
        model = usecase.create(request.data.get('text'))
        return model

