from narratorpro.application.application import Application

from narratorpro.core.services.service_locator import ServiceLocator
from narratorpro.core.services.configuration_service import ConfigurationService
from narratorpro.core.services.logging_service import LoggingService

def run() -> int:
    app = Application()
    return app.run()

services = ServiceLocator()

services.register(
    "config",
    ConfigurationService()
)

services.register(
    "logger",
    LoggingService()
)