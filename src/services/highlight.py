from typing import List

from ..clients.readwise import ReadwiseClient
from ..errors import ApiServerError
from ..models.highlight import Highlight

_readwise_client = ReadwiseClient()


async def get_highlights() -> List[Highlight]:
    raw_data = await _readwise_client.get_highlights()

    if not raw_data or "results" not in raw_data:
        raise ApiServerError("Unexpected response from Readwise API")

    results = raw_data["results"]

    if not isinstance(results, list):
        raise ApiServerError("Unexpected response format: results is not a list")

    highlights = [
        Highlight.from_dict(item) for item in results if isinstance(item, dict)
    ]

    return highlights
