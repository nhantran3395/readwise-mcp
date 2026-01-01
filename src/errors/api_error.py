from typing import Optional


class ApiError(Exception):
    """Base exception for platform-related errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_text: Optional[str] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.response_text = response_text
        super().__init__(self.message)


class ApiClientError(ApiError):
    """Exception raised for 4xx HTTP status codes."""

    pass


class ApiServerError(ApiError):
    """Exception raised for 5xx HTTP status codes."""

    pass


class ApiTimeoutError(ApiError):
    """Exception raised for timeout errors."""

    pass


class ApiInvalidResponseError(ApiError):
    """Exception raised for invalid responses."""

    pass
