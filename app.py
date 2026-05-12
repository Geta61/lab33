from src.infrastructure.factory_loader import load_factory
from src.services.notification_service import NotificationService


factory = load_factory()

service = NotificationService(factory)

service.notify("Request created")
