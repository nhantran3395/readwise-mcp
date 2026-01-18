from typing import List

from ..clients.readwise import ReadwiseClient
from ..errors import ApiServerError
from ..models.highlight import Highlight


class HighlightService:
    def __init__(self, client: ReadwiseClient):
        self.client = client

    async def get_highlights(self) -> List[Highlight]:
        raw_data = await self.client.get_highlights()

        if not raw_data or "results" not in raw_data:
            raise ApiServerError("Unexpected response from Readwise API")

        results = raw_data["results"]

        if not isinstance(results, list):
            raise ApiServerError("Unexpected response format: results is not a list")

        highlights = [
            Highlight.from_dict(item) for item in results if isinstance(item, dict)
        ]

        return highlights
