import json
import unittest
from pathlib import Path

import yaml
from jsonschema import ValidationError, validate


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema" / "permission-card.schema.json"
EXAMPLE_JSON = ROOT / "examples" / "price-check.json"
MISSING_GOAL = ROOT / "tests" / "fixtures" / "missing-goal.json"
TEMPLATE_JSON = ROOT / "templates" / "permission-card.json"
TEMPLATE_YAML = ROOT / "templates" / "permission-card.yaml"
TEMPLATE_MARKDOWN = ROOT / "templates" / "permission-card.md"
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


class PermissionCardSchemaTests(unittest.TestCase):
    def test_json_example_matches_schema(self):
        validate(instance=load_json(EXAMPLE_JSON), schema=load_json(SCHEMA))

    def test_missing_goal_is_rejected(self):
        with self.assertRaises(ValidationError):
            validate(instance=load_json(MISSING_GOAL), schema=load_json(SCHEMA))

    def test_json_and_yaml_templates_have_the_six_fields(self):
        json_template = load_json(TEMPLATE_JSON)
        yaml_template = yaml.safe_load(TEMPLATE_YAML.read_text(encoding="utf-8"))
        self.assertEqual(set(json_template), REQUIRED_FIELDS)
        self.assertEqual(set(yaml_template), REQUIRED_FIELDS)

    def test_markdown_template_has_a_heading_for_each_field(self):
        markdown = TEMPLATE_MARKDOWN.read_text(encoding="utf-8")
        for field in REQUIRED_FIELDS:
            self.assertIn(f"## {field}\n", markdown)


if __name__ == "__main__":
    unittest.main()
