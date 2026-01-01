from typing import List

from ..clients.readwise import ReadwiseClient
from ..errors import ApiServerError
from ..models.highlight import Highlight

_readwise_client = ReadwiseClient()

async def get_highlights() -> List[Highlight]:
    raw_data = await _readwise_client.get_highlights()

    if not raw_data or "results" not in raw_data:
        raise ApiServerError("Unexpected response from Readwise API")

    highlights = [Highlight.from_dict(item) for item in raw_data["results"]]

    return highlights
