from .base_channel import BaseChannel
from datetime import datetime

class SMSChannel(BaseChannel):

    def send(self, notification):

        message = notification["message"]

        if len(message) > 160:
            raise ValueError("SMS excede 160 caracteres")

        print(f"[SMS] Enviado a {notification['recipient']}")

        return {
            "status": "sent",
            "channel": "sms"
        }
