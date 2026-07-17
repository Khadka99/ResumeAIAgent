from core.utils.json_parser import parse_json


def test_parse_plain_json():

    data = parse_json(
        '{"company":"Brandt"}'
    )

    assert data["company"] == "Brandt"


def test_parse_markdown_json():

    text = """
```json
{
    "company":"Brandt"
}"""