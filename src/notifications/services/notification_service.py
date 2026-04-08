from src.notifications.services.sender_service import SenderService
from src.notifications.repositories.notification_repository import NotificationRepository
from fastapi import HTTPException



class NotificationService:

    def __init__(self, repository, sender_service):
        self.repository = repository
        self.sender_service = sender_service

    def create_notification(self, db, data, user_id):

        notification = self.repository.create(
            db=db,
            title=data.title,
            message=data.message,
            channel=data.channel,
            recipient=data.recipient,
            user_id=user_id
        )

        try:
            success = self.sender_service.send(notification)

            if success:
                notification.status = "sent"
            else:
                notification.status = "failed"

        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        except Exception:
            notification.status = "failed"

        db.commit()
        db.refresh(notification)

        return notification

