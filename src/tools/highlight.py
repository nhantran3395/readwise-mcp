from typing import List

from ..mcp_instance import mcp
from ..models.highlight import Highlight

from ..services.highlight import get_highlights


@mcp.tool
async def list_highlights() -> List[Highlight]:
    """
    List all highlights made by the user.

    Returns:
        A list of highlights.
    """
    highlights = await get_highlights()
    return highlights
