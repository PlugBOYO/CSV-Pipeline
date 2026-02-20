from abc import ABC, abstractmethod
from models.data_record import DataRecord

class ProcessingStrategy(ABC):
    """Abstract strategy for processing DataRecords."""

    @abstractmethod
    def process(self, record: DataRecord):
        pass
