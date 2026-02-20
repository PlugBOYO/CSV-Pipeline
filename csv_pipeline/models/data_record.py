class DataRecord:
    """Represents a single data record with an ID and a value."""
    def __init__(self, record_id: str, value: str):
        self.id = record_id
        self.value = value

    def __repr__(self):
        return f"DataRecord(id='{self.id}', value='{self.value}')"
