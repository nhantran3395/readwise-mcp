from typing import List

from ..clients.readwise import ReadwiseClient
from ..models import Highlight, Tag


class HighlightService:
    def __init__(self, client: ReadwiseClient):
        self.client = client

    async def get_highlights(self) -> List[Highlight]:
        highlights = await self.client.get_highlights()
        return highlights

    async def list_tags(self) -> List[Tag]:
        tags = await self.client.get_tags()
        return tags
