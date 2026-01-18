import pytest
from unittest.mock import AsyncMock, MagicMock

from errors import ApiServerError
from services.highlight import HighlightService


@pytest.fixture
def mock_readwise_client():
    """Provides a fresh AsyncMock for the ReadwiseClient."""
    return AsyncMock()


@pytest.fixture
def highlight_service(mock_readwise_client):
    """Provides an instance of HighlightService with the mocked client injected."""
    return HighlightService(client=mock_readwise_client)


class TestHighlightService:
    @pytest.mark.asyncio
    async def test_get_highlights_success_when_client_return_valid_response(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_highlights.return_value = {
            "results": [{"text": "Testing is fun", "author": "Dev"}]
        }

        results = await highlight_service.get_highlights()

        mock_readwise_client.get_highlights.assert_called_once()
        assert len(results) == 1

    @pytest.mark.asyncio
    async def test_get_highlights_api_server_error_is_propagated_when_api_response_does_not_contain_results_field(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_highlights.side_effect = ApiServerError(
            "Unexpected response from Readwise API"
        )

        with pytest.raises(
            ApiServerError, match="Unexpected response from Readwise API"
        ):
            await highlight_service.get_highlights()

    @pytest.mark.asyncio
    async def test_get_highlights_api_server_error_is_propagated_when_results_field_in_api_response_is_not_in_expected_format(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_highlights.side_effect = ApiServerError(
            "Unexpected response from Readwise API"
        )

        with pytest.raises(
            ApiServerError, match="Unexpected response from Readwise API"
        ):
            await highlight_service.get_highlights()

    @pytest.mark.asyncio
    async def test_list_tags_success_when_client_return_valid_response(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_tags.return_value = {
            "results": [{"name": "pytest", "key": "pytest"}]
        }

        results = await highlight_service.list_tags()

        mock_readwise_client.get_tags.assert_called_once()
        assert len(results) == 1

    @pytest.mark.asyncio
    async def test_list_tags_api_server_error_is_propagated_when_api_response_does_not_contain_results_field(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_tags.side_effect = ApiServerError(
            "Unexpected response from Readwise API"
        )

        with pytest.raises(
            ApiServerError, match="Unexpected response from Readwise API"
        ):
            await highlight_service.list_tags()

    @pytest.mark.asyncio
    async def test_list_tags_api_server_error_is_propagated_when_results_field_in_api_response_is_not_in_expected_format(
        self, highlight_service: HighlightService, mock_readwise_client: MagicMock
    ):
        mock_readwise_client.get_tags.side_effect = ApiServerError(
            "Unexpected response from Readwise API"
        )

        with pytest.raises(
            ApiServerError, match="Unexpected response from Readwise API"
        ):
            await highlight_service.list_tags()
