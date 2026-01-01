from fastmcp import FastMCP

mcp = FastMCP("Readwise MCP Server")


@mcp.tool
def say_hi(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello there, {name}!"
