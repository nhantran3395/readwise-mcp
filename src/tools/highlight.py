from typing import List

from clients.readwise import ReadwiseClient
from mcp_instance import mcp
from models.highlight import Highlight, Tag

from services.highlight import HighlightService


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


@mcp.tool
async def list_tags() -> List[Tag]:
    """
    List all tags created by the user.

    Returns:
        A list of tag names.
    """
    readwise_client = ReadwiseClient()
    tags = await HighlightService(client=readwise_client).list_tags()
    return tags
