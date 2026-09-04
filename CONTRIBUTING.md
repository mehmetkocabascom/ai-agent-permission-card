# Contributing

Small fixes and new fictional examples are welcome.

Before opening a pull request:

1. Remove or redact credentials, customer data, private URLs, internal paths, and confidential details.
2. Keep examples fictional. Use `example.com` for domains.
3. Update the JSON Schema and tests together if a field changes.
4. Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_examples.py`.
5. Explain why the change makes the card easier to use or verify.

Do not add telemetry, remote calls, executable agents, promotional link drops, generated secrets, or dependencies that are unrelated to validation.
