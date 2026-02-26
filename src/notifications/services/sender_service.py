from src.notifications.channels.email_channel import EmailChannel
from src.notifications.channels.sms_channel import SMSChannel
from src.notifications.channels.push_channel import PushChannel

class SenderService:

    _channels = {
        "email": EmailChannel(),
        "sms": SMSChannel(),
        "push": PushChannel(),
    }

    @classmethod
    def send(cls, channel_name, notification):

        channel = cls._channels.get(channel_name)

        if not channel:
            raise ValueError("Canal no soportado")

        return channel.send(notification)
