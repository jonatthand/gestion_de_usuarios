from src.notifications.services.sender_service import SenderService
from src.notifications.repositories.notification_repository import NotificationRepository

def create_notification(self, user_email, data):

    notification = NotificationRepository.create(
        user_email=user_email,
        title=data.title,
        message=data.message,
        recipient=data.recipient,
        channel=data.channel
    )

    SenderService.send(data.channel, notification)

    return notification

