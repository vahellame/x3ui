# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-08-25

Reshapes the package around a hand-written facade and enriches the specification
before generation. Existing code that imported endpoint modules directly needs
its import paths updated.

### Added

- `Panel`, a high-level client covering authentication and the common inbound,
  client and server operations. Methods return the payload directly instead of
  the `{success, msg, obj}` envelope.
- `X3uiError` and `NotAuthenticated`, raised when the panel reports a failure,
  carrying the panel's message and the operation that produced it.
- `Panel.login()`, which fetches a CSRF token before submitting credentials. The
  panel answers an empty `403` to any POST without that header, including the
  login request itself.
- `tools/infer_obj_schemas.py`, which fills undescribed response and request
  schemas from the examples already present in the document. Types 61 responses
  and 43 request bodies that were previously `Any`, hoisting inferred object
  schemas into named components so models read as `ServerStatus` and
  `ClientsListItem` rather than `GetPanelApiServerStatusResponse200Obj`.
- Context-manager support and `Panel.close()`.
- `x3ui.__version__`.
- `py.typed` marker at the package root.

### Changed

- The generated client moved from `x3ui` to `x3ui._generated`. Import endpoint
  modules from `x3ui._generated.api.<group>` and pass `panel.raw` as the client.
- `regenerate.sh` now enriches the specification, resets the `servers` entry so a
  panel's base path cannot be committed by accident, and rebuilds only
  `x3ui._generated`.
- Request bodies that were empty models — including `clients/add` and
  `inbounds/setEnable` — now carry their fields, so those operations are usable.

### Known limitations

- The facade is synchronous. Async callers use the generated `asyncio` variants.
- 101 responses carry no example in the specification and stay `Any`.

## [1.0.1] - 2026-08-25

### Fixed

- Corrected the session-authentication example in the documentation.

## [1.0.0] - 2026-08-25

First stable release: typed client for 186 operations, sync and async variants,
bearer token and session cookie authentication.

### Fixed

- Declared the `typing-extensions` runtime dependency required by the generated
  models. Earlier releases failed to import in a clean environment.

[2.0.0]: https://github.com/vahellame/x3ui/releases/tag/v2.0.0
[1.0.1]: https://github.com/vahellame/x3ui/releases/tag/v1.0.1
[1.0.0]: https://github.com/vahellame/x3ui/releases/tag/v1.0.0
