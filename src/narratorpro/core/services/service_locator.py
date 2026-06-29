from typing import Any


class ServiceLocator:
    """Simple dependency injection container."""

    def __init__(self):
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any):
        self._services[name] = service

    def resolve(self, name: str):
        return self._services[name]

    def contains(self, name: str):
        return name in self._services