"""
Configuration for the Readwise MCP Server.
"""

from dotenv import load_dotenv
from enum import Enum

load_dotenv()


# API Endpoints
class ApiEndpoint(Enum):
    pass


# Configuration
class Config:
    NETWORK_REQUEST_TIMEOUT = 180  # seconds
