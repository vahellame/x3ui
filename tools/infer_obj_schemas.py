#!/usr/bin/env python3
"""Fill in untyped `obj` response fields in the 3x-ui OpenAPI document.

The panel emits every response as {success, msg, obj} but leaves `obj` as an
empty schema, so a generated client types every payload as Any. Most operations
do carry a response `example`, which is enough to infer a usable schema.

Reads openapi.json, writes it back in place. Idempotent: an `obj` that already
has a schema is never touched.
"""

import json
import re
import sys
from pathlib import Path

METHODS = ("get", "post", "put", "delete", "patch")


def infer(value):
    if isinstance(value, bool):
        return {"type": "boolean"}
    if isinstance(value, int):
        return {"type": "integer", "format": "int64"}
    if isinstance(value, float):
        return {"type": "number"}
    if isinstance(value, str):
        return {"type": "string"}
    if isinstance(value, list):
        if not value:
            return None
        item = infer(value[0])
        if item is None:
            return None
        return {"type": "array", "items": item}
    if isinstance(value, dict):
        if not value:
            return None
        props = {}
        for key, sub in value.items():
            if sub is None:
                props[key] = {"nullable": True}
                continue
            inferred = infer(sub)
            if inferred is None:
                props[key] = {}
            else:
                props[key] = inferred
        return {"type": "object", "properties": props}
    return None


def model_name(route, suffix=""):
    cleaned = route.strip("/")
    cleaned = re.sub(r"^panel/api/", "", cleaned)
    cleaned = re.sub(r"\{[^}]+\}", "", cleaned)
    parts = [p for p in re.split(r"[/\-_.]", cleaned) if p]
    name = "".join(p[:1].upper() + p[1:] for p in parts)
    name = re.sub(r"[^0-9A-Za-z]", "", name) or "Payload"
    return name + suffix


def register(spec, name, schema):
    """Hoist an inline object schema into components/schemas and return a $ref."""
    if schema.get("type") != "object":
        return schema
    schemas = spec.setdefault("components", {}).setdefault("schemas", {})
    candidate = name
    counter = 2
    while candidate in schemas and schemas[candidate] != schema:
        candidate = f"{name}{counter}"
        counter += 1
    schemas[candidate] = schema
    return {"$ref": f"#/components/schemas/{candidate}"}


def fill_responses(spec):
    filled = skipped = already = 0
    for route, item in spec.get("paths", {}).items():
        for method, operation in item.items():
            if method not in METHODS:
                continue
            body = (
                operation.get("responses", {})
                .get("200", {})
                .get("content", {})
                .get("application/json", {})
            )
            schema = body.get("schema") or {}
            props = schema.get("properties") or {}
            if "obj" not in props:
                continue
            if props["obj"]:
                already += 1
                continue

            example = body.get("example")
            payload = example.get("obj") if isinstance(example, dict) else None
            inferred = infer(payload) if payload is not None else None

            if inferred is None:
                skipped += 1
                continue

            if inferred.get("type") == "object":
                inferred = register(spec, model_name(route), inferred)
            elif inferred.get("type") == "array" and inferred["items"].get("type") == "object":
                inferred["items"] = register(
                    spec, model_name(route) + "Item", inferred["items"]
                )

            props["obj"] = inferred
            filled += 1
    return filled, skipped, already


def fill_request_bodies(spec):
    filled = skipped = already = 0
    for route, item in spec.get("paths", {}).items():
        for method, operation in item.items():
            if method not in METHODS:
                continue
            body = (
                operation.get("requestBody", {})
                .get("content", {})
                .get("application/json", {})
            )
            if not body:
                continue
            schema = body.get("schema") or {}
            if schema.get("properties") or schema.get("items"):
                already += 1
                continue

            inferred = infer(body.get("example"))
            if inferred is None:
                skipped += 1
                continue

            if inferred.get("type") == "object":
                inferred = register(spec, model_name(route, "Request"), inferred)

            body["schema"] = inferred
            filled += 1
    return filled, skipped, already


def main(path):
    spec = json.loads(path.read_text())

    r_filled, r_skipped, r_already = fill_responses(spec)
    b_filled, b_skipped, b_already = fill_request_bodies(spec)

    path.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")

    print(f"responses:      filled {r_filled}, untyped {r_skipped}, already typed {r_already}")
    print(f"request bodies: filled {b_filled}, untyped {b_skipped}, already typed {b_already}")


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "openapi.json")
    if not target.exists():
        sys.exit(f"{target} not found")
    main(target)
