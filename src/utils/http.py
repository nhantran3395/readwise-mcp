"""
HTTP client utilities for the Readwise MCP Server.

This module provides pure HTTP client functionality for making API requests.
"""

import httpx

import logging
from typing import Dict, Optional, List, Union

from ..config import Config
from ..errors import ApiClientError, ApiServerError, ApiTimeoutError


logger = logging.getLogger(__name__)

# Global HTTP client for connection pooling
http_client = None


async def _initialize_client():
    """Initialize the global HTTP client."""
    global http_client
    if http_client is None:
        http_client = httpx.AsyncClient(
            timeout=Config.NETWORK_REQUEST_TIMEOUT,
            limits=httpx.Limits(max_keepalive_connections=10),
        )
    return http_client


async def _cleanup_client():
    """Clean up the global HTTP client."""
    global http_client
    if http_client is not None:
        await http_client.aclose()
        http_client = None


async def make_request(
    endpoint: str,
    method: str = "GET",
    params: Optional[Dict] = None,
    json_payload: Optional[Union[Dict, List]] = None,
    base_url: str = "",
    headers: Optional[Dict] = None,
):
    """
    Make an API request.

    Args:
        endpoint: The API endpoint to call.
        method: HTTP method (GET, POST, PUT, etc.).
        params: Optional query parameters.
        json_payload: Optional JSON body to send with the request.
        base_url: Base URL for the API.
        headers: Optional headers to include in the request.

    Returns:
        The JSON response or an error response dictionary.
    """
    try:
        url = f"{base_url}{endpoint}"

        headers = headers or {}
        headers["Content-Type"] = "application/json"

        # Use global client
        client = await _initialize_client()

        logger.debug(f"Sending {method} to {endpoint}: {headers}")

        # Make request based on method
        if method.upper() == "GET":
            response = await client.get(url, params=params, headers=headers)
        elif method.upper() == "POST":
            response = await client.post(
                url, params=params, json=json_payload, headers=headers
            )
        elif method.upper() == "PUT":
            response = await client.put(
                url, params=params, json=json_payload, headers=headers
            )
        elif method.upper() == "DELETE":
            response = await client.delete(url, params=params, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        logger.debug(f"{method} response from {endpoint}: {response.status_code}")

        response.raise_for_status()

        # Handle 204 No Content - successful request with no response body
        if response.status_code == 204:
            return {"status": "success", "status_code": 204, "message": "No content"}

        # Otherwise, parse and return JSON
        return response.json()

    except httpx.HTTPStatusError as e:
        logger.error(
            f"HTTP error {e.response.status_code} for {endpoint}: {e.response.text}"
        )
        if 400 <= e.response.status_code < 500:
            raise ApiClientError(
                f"HTTP error: {e.response.status_code}",
                status_code=e.response.status_code,
                response_text=e.response.text,
            )
        elif e.response.status_code >= 500:
            raise ApiServerError(
                f"HTTP error: {e.response.status_code}",
                status_code=e.response.status_code,
                response_text=e.response.text,
            )
    except httpx.TimeoutException as e:
        logger.error(f"Request timeout for {endpoint}: {str(e)}")
        raise ApiTimeoutError(
            f"Request timed out after {Config.NETWORK_REQUEST_TIMEOUT} seconds"
        )
    except Exception as e:
        logger.error(f"Unexpected error for {endpoint}: {str(e)}")
        raise Exception(f"Unexpected error for {endpoint}: {str(e)}")
