import json
from pydantic import BaseModel as PydanticBase, Field
from datetime import datetime
from pendulum import now
from typing import Dict


class BaseModel(PydanticBase):
    id: str = None
    created_at: datetime = Field(default_factory=now)
    deleted_at: datetime = None

    def delete(self):
        self.deleted_at = now()

    def to_dict(self) -> Dict:
        return self.dict()

    def to_json(self) -> bytes:
        return json.dumps(self.to_dict())
