from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional


@dataclass
class NoteEntity:
    id: Optional[int]
    title: Optional[str]
    body: str
    emoji: Optional[str]
    background_image: Optional[str]
    background_color: Optional[str]
    is_favorite: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def to_dict(self):
        return asdict(self)
