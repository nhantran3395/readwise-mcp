"""
Configuration for the Readwise MCP Server.
"""

import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()


# API Endpoints
class ApiEndpoint(Enum):
    HIGHLIGHTS = "/v2/highlights"
    TAGS = "/v3/tags"


# Configuration
class Config:
    NETWORK_REQUEST_TIMEOUT = 180  # seconds
    READWISE_API_BASE_URL = "https://readwise.io/api"
    READWISE_API_KEY = os.getenv("READWISE_API_KEY")
