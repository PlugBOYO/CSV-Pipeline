import csv
from models.data_record import DataRecord
from processor.data_processor import DataProcessor
from strategy.concrete_strategies import (
    DoubleValueStrategy,
    NegativeCheckStrategy,
    UppercaseStrategy,
)

INPUT_FILE = "data/input.csv"
OUTPUT_FILE = "data/output.csv"

def read_csv(file_path: str) -> list[DataRecord]:
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [DataRecord(row["id"], row["value"]) for row in reader]

def write_csv(file_path: str, records):
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["id", "value"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({"id": record.id, "value": record.value})

def main():
    records = read_csv(INPUT_FILE)

    strategies = [
        DoubleValueStrategy(),
        NegativeCheckStrategy(),
        UppercaseStrategy(),
    ]

    processor = DataProcessor(strategies)
    processed_records = processor.process_records(records)

    write_csv(OUTPUT_FILE, processed_records)

    for record in read_csv(OUTPUT_FILE):
        print(record)

if __name__ == "__main__":
    main()
