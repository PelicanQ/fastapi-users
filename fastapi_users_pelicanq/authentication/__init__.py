from fastapi_users_pelicanq.authentication.authenticator import Authenticator
from fastapi_users_pelicanq.authentication.backend import AuthenticationBackend
from fastapi_users_pelicanq.authentication.strategy import JWTStrategy, Strategy

try:
    from fastapi_users_pelicanq.authentication.strategy import RedisStrategy
except ImportError:  # pragma: no cover
    pass

from fastapi_users_pelicanq.authentication.transport import (
    BearerTransport,
    CookieTransport,
    Transport,
)

__all__ = [
    "Authenticator",
    "AuthenticationBackend",
    "BearerTransport",
    "CookieTransport",
    "JWTStrategy",
    "RedisStrategy",
    "Strategy",
    "Transport",
]
