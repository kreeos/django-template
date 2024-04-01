from __future__ import annotations
from dataclasses import dataclass
from sample_app.domain.models import SampleModel

@dataclass
class SampleDTO:
    name: str
    
    def __init__(self, text: str) -> None:
        self.text = text
        
    def from_model(model: SampleModel) -> SampleDTO:
        return SampleDTO(text=model.text)

    def to_dict(self) -> dict:
        return {
            'text': self.text
        }