from .base_channel import BaseChannel
from datetime import datetime

class PushChannel(BaseChannel):

    def send(self, notification):

        device_token = notification["recipient"]

        if not device_token:
            raise ValueError("Token inválido")

        payload = {
            "title": notification["title"],
            "body": notification["message"]
        }

        print(f"[PUSH] Enviado con payload {payload}")

        return {
            "status": "sent",
            "channel": "push"
        }
