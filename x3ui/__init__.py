"""Typed Python client for the 3x-ui panel API.

Two layers are available:

``Panel`` is the high-level interface and covers the common operations. It
handles authentication, unwraps the panel's ``{success, msg, obj}`` envelope,
and raises on failures.

Everything else is reachable through the generated layer under ``x3ui.api``,
using ``Panel.raw`` (or a ``Client`` built by hand) as the client argument.
"""

from importlib.metadata import PackageNotFoundError, version

from ._generated import AuthenticatedClient, Client
from ._generated.errors import UnexpectedStatus
from ._generated.types import UNSET, Response, Unset
from .panel import NotAuthenticated, Panel, X3uiError

try:
    __version__ = version("x3ui")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = (
    "AuthenticatedClient",
    "Client",
    "NotAuthenticated",
    "Panel",
    "Response",
    "UNSET",
    "UnexpectedStatus",
    "Unset",
    "X3uiError",
    "__version__",
)
