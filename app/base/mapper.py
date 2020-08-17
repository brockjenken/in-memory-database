from typing import List


class BaseMapper:
    def __init__(self, db):
        self.db = db

    def get_all(self) -> List:
        raise NotImplemented

    def get(self, obj_id: str) -> object:
        raise NotImplemented

    def create(self, obj: object) -> bool:
        raise NotImplemented

    def update(self, obj: object) -> bool:
        raise NotImplemented

    def delete(self, obj: object) -> bool:
        raise NotImplemented
