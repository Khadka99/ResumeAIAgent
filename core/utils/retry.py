"""
Retry utilities for API calls.
"""

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from openai import (
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
)


retry_api = retry(
    retry=retry_if_exception_type(
        (
            APIConnectionError,
            APITimeoutError,
            RateLimitError,
        )
    ),
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=1,
        max=8,
    ),
    reraise=True,
)