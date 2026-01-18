from dataclasses import dataclass
from typing import Dict


@dataclass
class Tag:
    name: str

    @classmethod
    def from_dict(cls, data: Dict) -> "Tag":
        return cls(name=data["name"])
