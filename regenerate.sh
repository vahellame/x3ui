#!/usr/bin/env bash
set -euo pipefail

SPEC="openapi.json"
PACKAGE="x3ui/_generated"

if [ "${1:-}" = "--fetch" ]; then
    if [ -z "${PANEL_URL:-}" ]; then
        echo "PANEL_URL is not set" >&2
        echo "usage: PANEL_URL=https://panel.example.com:2053/basepath PANEL_TOKEN=... ./regenerate.sh --fetch" >&2
        exit 1
    fi
    echo "Fetching spec from ${PANEL_URL}"
    curl -fsSL \
        ${PANEL_TOKEN:+-H "Authorization: Bearer ${PANEL_TOKEN}"} \
        "${PANEL_URL}/panel/api/openapi.json" \
        -o "${SPEC}"
fi

if [ ! -f "${SPEC}" ]; then
    echo "${SPEC} not found" >&2
    exit 1
fi

echo "Scrubbing panel-specific values"
python3 - "${SPEC}" << 'PY'
import json, sys
path = sys.argv[1]
spec = json.load(open(path))
before = spec.get("servers")
spec["servers"] = [{"description": "Current panel", "url": "/"}]
json.dump(spec, open(path, "w"), indent=2, ensure_ascii=False)
open(path, "a").write("\n")
if before != spec["servers"]:
    print("  servers reset (was panel-specific, never commit that)")
PY

echo "Inferring schemas from examples"
python3 tools/infer_obj_schemas.py "${SPEC}"

if ! command -v openapi-python-client >/dev/null 2>&1; then
    echo "openapi-python-client not found, installing" >&2
    pip install openapi-python-client
fi

echo "Generating ${PACKAGE}"
rm -rf "${PACKAGE}"
openapi-python-client generate \
    --path "${SPEC}" \
    --meta none \
    --output-path "${PACKAGE}" \
    --overwrite

echo
echo "Done. The hand-written facade in x3ui/__init__.py and x3ui/panel.py is untouched."
echo "Review the diff before committing:"
echo "  git diff --stat"
