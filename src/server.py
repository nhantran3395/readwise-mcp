from starlette.middleware.cors import CORSMiddleware

from .tools import *
from .mcp_instance import mcp

app = mcp.http_app(transport="streamable-http")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
