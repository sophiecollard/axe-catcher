import json
from typing import Any

from .model import Config

def read_config(path: str) -> Config:
    raw_json = _read_file_contents(path)
    parsed_json = _parse_json(raw_json)
    config = Config.decode_from(parsed_json)
    return config

def _read_file_contents(path: str) -> str:
    with open(path) as f:
        contents = f.read()
        f.close()
        return contents

def _parse_json(raw_json: str) -> dict[str, Any]:
    parsed_json = json.loads(raw_json)
    return parsed_json
