from ..utils.http import make_request
from ..config import Config, ApiEndpoint


class ReadwiseClient:
    def __init__(self):
        self.base_url = Config.READWISE_API_BASE_URL
        self.headers = {"Authorization": f"Token {Config.READWISE_API_KEY}"}

    async def get_highlights(self):
        response = await make_request(
            endpoint=ApiEndpoint.HIGHLIGHTS.value,
            base_url=self.base_url,
            headers=self.headers,
        )
        return response
