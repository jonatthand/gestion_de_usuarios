from sqlalchemy.orm import Session
from src.notifications.models.notification_model import Notification


class NotificationRepository:

    @staticmethod
    def create(
        db: Session,
        title: str,
        message: str,
        channel: str,
        recipient: str,
        user_id: int
    ):
        notification = Notification(
            title=title,
            message=message,
            channel=channel,
            recipient=recipient,
            user_id=user_id
        )

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    @staticmethod
    def get_by_user(db: Session, user_id: int):
        return db.query(Notification).filter(Notification.user_id == user_id).all()
    
    @staticmethod
    def get_by_id(db: Session, notification_id: int):
        return db.query(Notification).filter(
        Notification.id == notification_id
        ).first()
    
    @staticmethod
    def update(db: Session, notification, data):

        if data.title is not None:
            notification.title = data.title

        if data.message is not None:
            notification.message = data.message

        if data.channel is not None:
            notification.channel = data.channel

        if data.recipient is not None:
            notification.recipient = data.recipient

        db.commit()
        db.refresh(notification)

        return notification 
    
    @staticmethod
    def delete(db: Session, notification):

        db.delete(notification)
        db.commit()