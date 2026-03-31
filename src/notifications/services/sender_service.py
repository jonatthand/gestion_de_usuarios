from src.notifications.strategies.email_sender import EmailSender
from src.notifications.strategies.sms_sender import SMSSender
from src.notifications.strategies.push_sender import PushSender


class SenderService:

    strategies = {
        "email": EmailSender(),
        "sms": SMSSender(),
        "push": PushSender()
    }

    @classmethod
    def send(cls, notification):

        sender = cls.strategies.get(notification.channel)

        if not sender:
            raise ValueError("Canal no soportado")

        return sender.send(notification)