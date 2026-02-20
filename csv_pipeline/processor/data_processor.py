from typing import List, Generator
from models.data_record import DataRecord
from strategy.processing_strategy import ProcessingStrategy

class DataProcessor:
    """Processes DataRecords using multiple strategies sequentially."""

    def __init__(self, strategies: List[ProcessingStrategy]):
        self.strategies = strategies

    def process_records(self, records: List[DataRecord]) -> Generator[DataRecord, None, None]:
        for record in records:
            for strategy in self.strategies:
                strategy.process(record)
            yield record
