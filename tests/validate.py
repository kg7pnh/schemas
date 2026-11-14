"""Check every schema in json/ and run the examples in tests/<schema>/{valid,invalid}/."""

import json
import pathlib
import sys

from jsonschema import Draft7Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent
schemas = {
    path.name.removesuffix(".schema.json"): json.loads(path.read_text(encoding="utf-8"))
    for path in sorted((ROOT / "json").glob("*.schema.json"))
}
registry = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
)

failures = 0
for name, schema in schemas.items():
    Draft7Validator.check_schema(schema)
    validator = Draft7Validator(schema, registry=registry)
    for expected in ("valid", "invalid"):
        for example in sorted((ROOT / "tests" / name / expected).glob("*.json")):
            errors = list(validator.iter_errors(json.loads(example.read_text(encoding="utf-8"))))
            ok = (not errors) if expected == "valid" else bool(errors)
            label = "ok  " if ok else "FAIL"
            print(f"{label} {name}/{expected}/{example.name}")
            if not ok:
                failures += 1
                for error in errors:
                    print(f"       {error.message}")

if failures:
    print(f"{failures} example(s) failed")
    sys.exit(1)
print("all examples passed")
