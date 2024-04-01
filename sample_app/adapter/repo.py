from sample_app.domain.models import SampleModel
from sample_app.service.interface import SampleRepository
import logging
class DjangoSampleRepository(SampleRepository):
    def get(self, id: int) -> SampleModel:
        logging.critical(f'id: {id}')
        try:
            return SampleModel.objects.get(id=id)
        except SampleModel.DoesNotExist:
            raise ValueError('Not Found')

    def create(self, text: str) -> SampleModel:
        sample_model = SampleModel()
        sample_model.text = text
        sample_model.save()
        return sample_model
