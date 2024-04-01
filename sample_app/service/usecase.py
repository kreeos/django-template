from sample_app.domain.models import SampleModel
from sample_app.service.interface import SampleRepository

class SampleUsecase:
    def __init__(self, repository: SampleRepository):
        self.repository = repository

    def get(self, id: int) -> SampleModel:
        return self.repository.get(id)

    def create(self, name: str) -> SampleModel:
        return self.repository.create(name)