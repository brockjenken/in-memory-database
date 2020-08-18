"""
This model represents a transaction. It stores the transaction's id, along with its key and value. It helps to
simplify defaulting None values and converting to dicts for storage.

When retrieving values from a transaction, it will return the new value if it exists, otherwise it will return
the initial value.
"""
from typing import Dict, Union

'''Constants'''
INITIAL_VALUE = "initial_value"
NEW_VALUE = "new_value"


class TransactionModel:
    def __init__(self, id: str = None, data: Dict[str, Dict[str, Union[str, None]]] = None):
        self.id = id
        self.data = data or {}

    def get_data(self) -> Dict:
        return self.data

    def initialize_data(self, data: Dict[str, str]):
        for k, v in data.items():
            self.data[k] = {INITIAL_VALUE: v}

    def get_value(self, key: str) -> str:
        data = self.data.get(key, {})

        if NEW_VALUE in data:
            return data[NEW_VALUE]

        return data.get(INITIAL_VALUE)

    def set_value(self, key: str, value: str):
        if key not in self.data:
            self.data[key] = {INITIAL_VALUE: None, NEW_VALUE: value}
        else:
            self.data[key][NEW_VALUE] = value

    def delete_value(self, key: str):
        if key in self.data:
            self.data[key][NEW_VALUE] = None

    def dict(self):
        return {
            "id": self.id,
            "data": self.data
        }
