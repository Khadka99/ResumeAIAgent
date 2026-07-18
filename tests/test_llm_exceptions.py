import pytest

from core import (
    LLMError,
    LLMConfigurationError,
    LLMProviderError,
    LLMResponseError,
    UnsupportedProviderError,
)


def test_exception_inheritance():
    assert issubclass(LLMConfigurationError, LLMError)
    assert issubclass(LLMProviderError, LLMError)
    assert issubclass(LLMResponseError, LLMError)
    assert issubclass(UnsupportedProviderError, LLMConfigurationError)


def test_raise_provider_error():
    with pytest.raises(LLMProviderError):
        raise LLMProviderError("Provider failed")


def test_raise_configuration_error():
    with pytest.raises(LLMConfigurationError):
        raise LLMConfigurationError("Invalid configuration")