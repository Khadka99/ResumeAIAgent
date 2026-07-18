import pytest

from core import OpenAILLM
from core import LLMResponse


def test_provider_name():

    llm = OpenAILLM()

    assert llm.provider_name == "OpenAI"


def test_model_name():

    llm = OpenAILLM()

    assert llm.model != ""


@pytest.mark.skip(reason="Requires OpenAI API credits")
def test_real_request():

    llm = OpenAILLM()

    response = llm.ask(
        "What is the capital of Canada?"
    )

    assert isinstance(response, LLMResponse)

    assert "Ottawa" in response.content