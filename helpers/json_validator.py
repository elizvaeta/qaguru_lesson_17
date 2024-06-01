import json

from config import JSON_SCHEMAS_DIR
from jsonschema.validators import validate
from requests import Response


def assert_json_schema(response: Response, schema_name: str) -> None:
    full_path = JSON_SCHEMAS_DIR + '/' + schema_name

    with open(full_path) as f:
        schema = json.load(f)

    validate(response.json(), schema)
