"""
Custom exceptions used throughout the Resume AI Agent.
"""


class LLMError(Exception):
    """
    Base exception for all LLM-related errors.
    """

    pass


class LLMConfigurationError(LLMError):
    """
    Raised when the LLM configuration is invalid.
    """

    pass


class LLMProviderError(LLMError):
    """
    Raised when an LLM provider fails to generate a response.
    """

    pass


class LLMResponseError(LLMError):
    """
    Raised when an LLM returns an invalid or empty response.
    """

    pass


class UnsupportedProviderError(LLMConfigurationError):
    """
    Raised when an unsupported provider is configured.
    """

    pass