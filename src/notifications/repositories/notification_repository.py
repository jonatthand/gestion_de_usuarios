from datetime import datetime
import uuid

class NotificationRepository:

    _db = []

    @classmethod
    def create(cls, user_email, title, message, recipient, channel):

        notification = {
            "id": str(uuid.uuid4()),
            "user_email": user_email,
            "title": title,
            "message": message,
            "recipient": recipient,
            "channel": channel,
            "created_at": datetime.utcnow(),
            "status": "created"
        }

        cls._db.append(notification)

        return notification

    @classmethod
    def list_by_user(cls, user_email):
        return [n for n in cls._db if n["user_email"] == user_email]
