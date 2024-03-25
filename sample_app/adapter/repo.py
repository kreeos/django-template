from sample_app.domain.models import SampleModel
from sample_app.service.interface import SampleRepository


class DjangoSampleRepository(SampleRepository):
    def get(self, id: int) -> SampleModel:
        try:
            SampleModel.objects.get(id)
        except SampleModel.DoesNotExist:
            return None

    def create(self, text: str) -> SampleModel:
        sample_model = SampleModel()
        sample_model.text = text
        return sample_model.save()
