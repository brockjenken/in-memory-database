from typing import Dict, Any, Union


class Collection:
    def __init__(self, name: str):
        self.data = {}
        self.name = name

        if self.name not in self.data:
            self.data[self.name] = {}

    def upsert(self, _id: str, data: Dict[str, Any]):
        self.data[self.name][_id] = data

    def find(self, _id: str) -> Union[Dict[str, Any], None]:
        return self.data[self.name].get(_id)


class InMemoryDB:
    def __getattr__(self, name: str) -> Collection:
        return Collection(name)


def setup() -> InMemoryDB:
    return InMemoryDB()
