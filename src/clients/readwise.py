from typing import List

from errors import ApiServerError
from models import Highlight, Tag, ApiResponse
from utils.http import make_request
from config import Config, ApiEndpoint


def _validate_response(response) -> ApiResponse:
    if response is None:
        raise ApiServerError("No response received from Readwise API")

    if not isinstance(response, dict):
        raise ApiServerError(f"Unexpected response type: {type(response)}")

    if "results" not in response:
        raise ApiServerError(
            "Unexpected response from Readwise API: missing 'results' key"
        )

    if not isinstance(response["results"], list):
        raise ApiServerError("Unexpected response format: results is not a list")

    return response


class ReadwiseClient:
    def __init__(self):
        self.base_url = Config.READWISE_API_BASE_URL
        self.headers = {"Authorization": f"Token {Config.READWISE_API_KEY}"}

    async def get_highlights(self) -> List[Highlight]:
        raw_response = await make_request(
            endpoint=ApiEndpoint.HIGHLIGHTS.value,
            base_url=self.base_url,
            headers=self.headers,
        )

        response = _validate_response(raw_response)

        results = response["results"]

        highlights = [
            Highlight.from_dict(item) for item in results if isinstance(item, dict)
        ]

        return highlights

    async def get_tags(self) -> List[Tag]:
        raw_response = await make_request(
            endpoint=ApiEndpoint.TAGS.value,
            base_url=self.base_url,
            headers=self.headers,
        )

        response = _validate_response(raw_response)

        results = response["results"]

        tags = [Tag.from_dict(item) for item in results if isinstance(item, dict)]

        return tags
