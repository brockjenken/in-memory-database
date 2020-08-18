"""
This model represents a transaction. It stores the transaction's id, along with its key and value. It helps to
simplify defaulting None values and converting to dicts for storage.

When retrieving values from a transaction, it will throw a KeyError if it tries to retrieve with a key that has not
been used yet to delete or modify a value.

Every time a value is set or deleted, the initial value is passed to help ensure a more secure transaction when
committing.
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

    def get_value(self, key: str) -> str:
        return self.data[key][INITIAL_VALUE]

    def set_value(self, key: str, initial_value: str, new_value: str):
        if key not in self.data:
            self.data[key] = {INITIAL_VALUE: initial_value, NEW_VALUE: new_value}
        else:
            self.data[key][NEW_VALUE] = new_value

    def delete_value(self, initial_value: str, key: str):
        if key not in self.data:
            self.data[key] = {INITIAL_VALUE: initial_value, NEW_VALUE: None}
        else:
            self.data[key][NEW_VALUE] = None

    def dict(self):
        return {
            "id": self.id,
            "data": self.data
        }
