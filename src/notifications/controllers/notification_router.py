from fastapi import APIRouter
from src.notifications.schemas.notification_schema import NotificationCreateSchema
from src.notifications.services.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/")
def create_notification(notification: NotificationCreateSchema):
    return NotificationService.create_notification(notification)
