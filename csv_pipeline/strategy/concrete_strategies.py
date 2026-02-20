from strategy.processing_strategy import ProcessingStrategy
from models.data_record import DataRecord

class DoubleValueStrategy(ProcessingStrategy):
    def process(self, record: DataRecord):
        try:
            record.value = str(int(record.value) * 2)
        except ValueError:
            record.value = "ERROR"

class NegativeCheckStrategy(ProcessingStrategy):
    def process(self, record: DataRecord):
        try:
            if int(record.value) < 0:
                record.value = "INVALID"
        except ValueError:
            record.value = "ERROR"

class UppercaseStrategy(ProcessingStrategy):
    def process(self, record: DataRecord):
        if not record.value.isdigit():
            record.value = record.value.upper()
