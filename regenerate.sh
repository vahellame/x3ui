#!/usr/bin/env bash
set -euo pipefail

SPEC="openapi.json"
PACKAGE="x3ui"

if [ "${1:-}" = "--fetch" ]; then
    if [ -z "${PANEL_URL:-}" ]; then
        echo "PANEL_URL is not set" >&2
        echo "usage: PANEL_URL=https://panel.example.com:2053 PANEL_TOKEN=... ./regenerate.sh --fetch" >&2
        exit 1
    fi
    echo "Fetching spec from ${PANEL_URL}"
    curl -fsSL \
        ${PANEL_TOKEN:+-H "Authorization: Bearer ${PANEL_TOKEN}"} \
        "${PANEL_URL}/panel/api/openapi.json" \
        -o "${SPEC}"
    echo "Saved to ${SPEC}"
fi

if [ ! -f "${SPEC}" ]; then
    echo "${SPEC} not found" >&2
    exit 1
fi

if ! command -v openapi-python-client >/dev/null 2>&1; then
    echo "openapi-python-client not found, installing" >&2
    pip install openapi-python-client
fi

echo "Generating ${PACKAGE} from ${SPEC}"
openapi-python-client generate \
    --path "${SPEC}" \
    --meta none \
    --output-path "${PACKAGE}" \
    --overwrite

echo
echo "Done. Review the diff before committing:"
echo "  git diff --stat"
