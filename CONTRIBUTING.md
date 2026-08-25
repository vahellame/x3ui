# Working on x3ui

The client is generated from the panel's own OpenAPI document with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
That document leaves most payloads undescribed, so the document is enriched
before generation.

## Layout

- `x3ui/panel.py` — the `Panel` convenience layer, written by hand.
- `x3ui/_generated/` — generated from `openapi.json`, never edited by hand.
- `tools/infer_obj_schemas.py` — enriches the document before generation.
- `tools/overrides.json` — hand-written schemas for endpoints the panel
  documents with neither schema nor example.

## Regenerating

```
./regenerate.sh
```

Against a live panel:

```
PANEL_URL=https://panel.example.com:2053/yourpath PANEL_TOKEN=... ./regenerate.sh --fetch
```

The script blanks the `servers` entry before writing the document, because one
fetched from a live panel contains that panel's secret path. Never commit it.

Regeneration replaces `x3ui/_generated` only. The hand-written facade survives.

## Enrichment

`tools/infer_obj_schemas.py` reads the `example` values already present in the
document and writes back the schemas it can infer, which types 61 responses and
43 request bodies that would otherwise be `Any`. Inferred object schemas are
hoisted into `components/schemas` under names derived from the route, so models
read as `ServerStatus` rather than `GetPanelApiServerStatusResponse200Obj`.

Endpoints with neither schema nor example need an entry in
`tools/overrides.json`. That is how `clients/get` and `clients/update` became
typed, and it is the most useful contribution to make: describing an endpoint
once turns a dict into a typed model for everyone.

## Releasing

Bump `version` in `pyproject.toml`, add a `CHANGELOG.md` entry, push, wait for
CI, then publish a GitHub release tagged `vX.Y.Z`. The publish workflow uploads
to PyPI through trusted publishing.
