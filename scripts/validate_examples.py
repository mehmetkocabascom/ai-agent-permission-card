#!/usr/bin/env python3
import json
from pathlib import Path

import yaml
from jsonschema import validate


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = {
    "goal",
    "may_read",
    "may_write",
    "ask_before",
    "stop_if",
    "show_me",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    schema = load_json(ROOT / "schema" / "permission-card.schema.json")
    example = load_json(ROOT / "examples" / "price-check.json")
    json_template = load_json(ROOT / "templates" / "permission-card.json")
    yaml_template = yaml.safe_load(
        (ROOT / "templates" / "permission-card.yaml").read_text(encoding="utf-8")
    )

    validate(instance=example, schema=schema)
    validate(instance=json_template, schema=schema)
    if set(json_template) != REQUIRED_FIELDS:
        raise ValueError("JSON template fields do not match the six-field contract")
    if set(yaml_template) != REQUIRED_FIELDS:
        raise ValueError("YAML template fields do not match the six-field contract")

    print("validation=PASS")


if __name__ == "__main__":
    main()
