# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-25

First stable release.

### Added

- Typed client for the 3x-ui panel API, generated from the panel's own OpenAPI
  document: 186 operations across inbounds, clients, nodes, hosts, server, settings,
  Xray settings, API tokens, backup, subscriptions and websocket endpoints.
- Synchronous and asynchronous variants for every operation, plus `_detailed`
  variants exposing status code, headers and raw content.
- Bearer token and session cookie authentication.
- Usage documentation covering authentication, common operations, async usage and
  client configuration.
- Continuous integration building and smoke-testing on Python 3.10 through 3.13.
- `regenerate.sh` for fetching the specification from a live panel and regenerating
  the client.

### Fixed

- Declared the `typing-extensions` runtime dependency required by the generated
  models. Earlier releases failed to import in a clean environment.

### Notes

- Response payloads arrive as `{success, msg, obj}` where `obj` is typed `Any` for
  most operations, because the upstream specification does not describe it.
- Requires Python 3.10 or newer.

[1.0.0]: https://github.com/vahellame/x3ui/releases/tag/v1.0.0
