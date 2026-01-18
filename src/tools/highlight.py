from typing import List

from ..clients.readwise import ReadwiseClient
from ..mcp_instance import mcp
from ..models.highlight import Highlight

from ..services.highlight import HighlightService


@mcp.tool
async def list_highlights() -> List[Highlight]:
    """
    List all highlights made by the user.

    Returns:
        A list of highlights.
    """
    readwise_client = ReadwiseClient()
    highlights = await HighlightService(client=readwise_client).get_highlights()
    return highlights
