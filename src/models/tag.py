from dataclasses import dataclass


@dataclass
class Tag:
    name: str

    @classmethod
    def from_dict(cls, data: dict) -> "Tag":
        return cls(name=data["name"])
