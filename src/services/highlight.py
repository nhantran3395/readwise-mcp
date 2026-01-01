from typing import List
import logging

from ..clients.readwise import ReadwiseClient
from ..errors import ApiServerError
from ..models.highlight import Highlight

_readwise_client = ReadwiseClient()

logger = logging.getLogger(__name__)

async def get_highlights() -> List[Highlight]:
    raw_data = await _readwise_client.get_highlights()

    logger.warning(f'get_highlights raw_data: {raw_data}')

    if not raw_data or "results" not in raw_data:
        raise ApiServerError("Unexpected response from Readwise API")

    highlights = [Highlight.from_dict(item) for item in raw_data["results"]]

    return highlights
