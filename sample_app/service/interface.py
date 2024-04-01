from abc import ABC, abstractmethod
from sample_app.domain.models import SampleModel


class SampleRepository(ABC):
    @abstractmethod
    def get(self, id: int) -> SampleModel:
        pass

    @abstractmethod
    def create(self, text: str) -> SampleModel:
        pass