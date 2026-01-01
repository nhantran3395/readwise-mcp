from dataclasses import dataclass
from typing import List

from .tag import Tag

@dataclass
class Highlight:
    text: str
    note: str
    tag: List[Tag]
    highlighted_at: str
    updated: str

    @classmethod
    def from_dict(cls, data: dict) -> "Highlight":
        tags = [Tag.from_dict(tag) for tag in data.get("tags", [])]
        return cls(
            text=data.get("text", ""),
            note=data.get("note", ""),
            tag=tags,
            highlighted_at=data.get("highlighted_at", ""),
            updated=data.get("updated", ""),
        )